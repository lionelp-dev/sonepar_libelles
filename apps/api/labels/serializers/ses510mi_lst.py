from rest_framework import serializers

from ..models import SES510MI_Lst


class SES510MI_LstSerializer(serializers.ModelSerializer):
    libelle_prgnu = serializers.CharField(read_only=True, allow_null=True)
    libelle_trans_program = serializers.CharField(read_only=True, allow_null=True)
    libelle_changed_fnc = serializers.CharField(read_only=True, allow_null=True)
    libelle_changed_role = serializers.CharField(read_only=True, allow_null=True)
    libelle_op_code = serializers.CharField(read_only=True, allow_null=True)
    libelle_option = serializers.CharField(read_only=True, allow_null=True)

    class Meta:
        model = SES510MI_Lst
        fields = (
            "trdt", "trtm", "usiu", "conu", "divu", "prgnu", "libelle_prgnu",
            "changed_by", "trans_program", "libelle_trans_program", "op_code", "libelle_op_code",
            "changed_role", "libelle_changed_role", "changed_fnc", "libelle_changed_fnc", "changed_user", "type_droit",
            "code_option", "libelle_option", "autorisee_avant", "autorisee_apres",
        )
