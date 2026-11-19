from rest_framework import serializers

from .models import (
    LibellesFonctions,
    LibellesOptions,
    MNS110MI_Lst,
    MNS150MI_LstUsers,
    MNS405MI_Lst,
    MNS410MI_LstRolesByUser,
    SES400MI_LstAuthByRole,
    SES401_CMNPUS,
    SES510MI_Lst,
)


class MNS150MI_LstUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNS150MI_LstUsers
        fields = ("user_id", "nom_complet", "statut")


class MNS110MI_LstSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNS110MI_Lst
        fields = (
            "code_fonction",
            "programme_m3",
            "categorie_fonction",
            "autorisation_requise",
        )


class MNS405MI_LstSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNS405MI_Lst
        fields = ("role_id", "nom_role", "description")


class MNS410MI_LstRolesByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNS410MI_LstRolesByUser
        fields = ("id", "user_id", "role_id")


class SES400MI_LstAuthByRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SES400MI_LstAuthByRole
        fields = (
            "id",
            "role_id",
            "code_fonction",
            "libelle_fonction",
            "societe",
            "division",
            "statut",
            "code_option",
        )


class LibellesFonctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibellesFonctions
        fields = ("code_fonction", "libelle_fonction", "description")


class SES401_CMNPUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SES401_CMNPUS
        fields = (
            "id",
            "user_id",
            "nom_complet",
            "programme_m3",
            "societe",
            "division",
            "role_id",
            "code_option",
        )


class LibellesOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibellesOptions
        fields = ("code_option", "libelle_option", "libelle_anglais", "description")


class SES510MI_LstSerializer(serializers.ModelSerializer):
    class Meta:
        model = SES510MI_Lst
        fields = (
            "id",
            "id_evenement",
            "trdt",
            "trtm",
            "usiu",
            "conu",
            "divu",
            "prgnu",
            "modifie_par",
            "programme_origine",
            "code_operation",
            "role_modifie",
            "fonction_modifiee",
            "utilisateur_modifie",
            "code_option",
            "autorisee_avant",
            "autorisee_apres",
            "options_de_base_modifiees",
            "options_associees_modifiees",
            "touches_fonction_modifiees",
        )
