from rest_framework import serializers

from ..models import LibelleProgramme


class LibelleProgrammeSerializer(serializers.ModelSerializer):
    def validate_code_programme(self, value):
        if self.instance is None and LibelleProgramme.objects.filter(code_programme=value).exists():
            raise serializers.ValidationError("Ce code de programme existe déjà.")
        return value

    class Meta:
        model = LibelleProgramme
        fields = ("code_programme", "libelle")
        extra_kwargs = {"libelle": {"allow_null": False, "allow_blank": False, "required": True}}
