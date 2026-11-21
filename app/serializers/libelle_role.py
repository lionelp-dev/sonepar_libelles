from rest_framework import serializers

from ..models import LibelleRole


class LibelleRoleSerializer(serializers.ModelSerializer):
    def validate_code_role(self, value):
        if self.instance is None and LibelleRole.objects.filter(code_role=value).exists():
            raise serializers.ValidationError("Ce code de rôle existe déjà.")
        return value

    class Meta:
        model = LibelleRole
        fields = ("code_role", "libelle")
        extra_kwargs = {"libelle": {"allow_null": False, "allow_blank": False, "required": True}}
