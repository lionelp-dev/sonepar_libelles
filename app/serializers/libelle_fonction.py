from rest_framework import serializers

from ..models import LibelleFonction


class LibelleFonctionSerializer(serializers.ModelSerializer):
    def validate_code_fonction(self, value):
        if self.instance is None and LibelleFonction.objects.filter(code_fonction=value).exists():
            raise serializers.ValidationError("Ce code de fonction existe déjà.")
        return value

    class Meta:
        model = LibelleFonction
        fields = ("code_fonction", "libelle")
        extra_kwargs = {"libelle": {"allow_null": False, "allow_blank": False, "required": True}}
