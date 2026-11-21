"""Logique métier de création et de mise à jour des libellés locaux."""


def create_label(*, serializer_class, data):
    serializer = serializer_class(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer


def upsert_label(*, code, data, model, serializer_class, code_field):
    instance = model.objects.filter(**{code_field: code}).first()
    serializer_data = {"libelle": data.get("libelle")}
    if instance is None:
        serializer_data[code_field] = code
    serializer = serializer_class(
        instance, data=serializer_data, partial=instance is not None
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer, instance is None
