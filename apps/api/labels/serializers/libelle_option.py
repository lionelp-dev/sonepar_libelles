from rest_framework import serializers

from ..models import LibelleOption


class LibelleOptionSerializer(serializers.ModelSerializer):
    def validate_code_option(self, value):
        if self.instance is None and LibelleOption.objects.filter(code_option=value).exists():
            raise serializers.ValidationError("Ce code d'option existe déjà.")
        return value

    class Meta:
        model = LibelleOption
        fields = ("code_option", "libelle")
        extra_kwargs = {"libelle": {"allow_null": False, "allow_blank": False, "required": True}}
