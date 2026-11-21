from rest_framework import serializers

from ..models import LibelleOpCode


class LibelleOpCodeSerializer(serializers.ModelSerializer):
    def validate_op_code(self, value):
        if self.instance is None and LibelleOpCode.objects.filter(op_code=value).exists():
            raise serializers.ValidationError("Ce code opération existe déjà.")
        return value

    class Meta:
        model = LibelleOpCode
        fields = ("op_code", "libelle")
        extra_kwargs = {"libelle": {"allow_null": False, "allow_blank": False, "required": True}}
