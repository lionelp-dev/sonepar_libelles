from rest_framework import serializers

from .models import (
    AuditHabilitations,
    Habilitations,
    LibellesFonctions,
    LibellesNiveauxAcces,
    LibellesOptions,
    MNS150MI_LstUsers,
    MNS405MI_Lst,
    MNS410MI_LstRolesByUser,
    SES400MI_LstAuthByRole,
)


class MNS150MI_LstUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MNS150MI_LstUsers
        fields = ("user_id", "nom_complet", "statut")


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
            "options_autorisees",
            "niveau_acces",
        )


class LibellesFonctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibellesFonctions
        fields = ("code_fonction", "libelle_fonction", "description")


class LibellesNiveauxAccesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibellesNiveauxAcces
        fields = ("niveau_acces", "libelle_niveau_acces", "description")


class LibellesOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibellesOptions
        fields = ("code_option", "libelle_option", "libelle_anglais", "description")


class AuditHabilitationsSerializer(serializers.ModelSerializer):
    habilitations_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = AuditHabilitations
        fields = ("id", "created_at", "habilitations_count")


class HabilitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilitations
        fields = (
            "id",
            "audit",
            "user_id",
            "nom_complet",
            "role_id",
            "nom_role",
            "code_fonction",
            "libelle_fonction",
            "societe",
            "division",
            "statut",
            "options_autorisees",
            "libelles_options_autorisees",
            "niveau_acces",
            "libelle_niveau_acces",
        )
