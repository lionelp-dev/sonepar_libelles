"""Logique partagée de génération et d'export des audits."""

from collections import defaultdict
import csv

from django.db import transaction

from app.models import (
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


AUDIT_EXPORT_FIELDS = (
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


@transaction.atomic
def generate_audit() -> tuple[AuditHabilitations, int]:
    """Crée un instantané enrichi des habilitations actuellement chargées."""
    audit = AuditHabilitations.objects.create()
    utilisateurs = {
        utilisateur.user_id: utilisateur.nom_complet
        for utilisateur in MNS150MI_LstUsers.objects.all()
    }
    roles = {role.role_id: role.nom_role for role in MNS405MI_Lst.objects.all()}
    fonctions = {
        fonction.code_fonction: fonction.libelle_fonction
        for fonction in LibellesFonctions.objects.all()
    }
    niveaux_acces = {
        niveau.niveau_acces: niveau.libelle_niveau_acces
        for niveau in LibellesNiveauxAcces.objects.all()
    }
    options_par_code = {
        str(option.code_option): option.libelle_option
        for option in LibellesOptions.objects.all()
    }

    autorisations_par_role = defaultdict(list)
    for autorisation in SES400MI_LstAuthByRole.objects.order_by("role_id", "code_fonction"):
        autorisations_par_role[autorisation.role_id].append(autorisation)

    nombre_habilitations = 0
    for affectation in MNS410MI_LstRolesByUser.objects.order_by("user_id", "role_id"):
        nom_complet = utilisateurs.get(
            affectation.user_id,
            f"Utilisateur inconnu ({affectation.user_id})",
        )
        nom_role = roles.get(affectation.role_id, f"Rôle inconnu ({affectation.role_id})")

        for autorisation in autorisations_par_role[affectation.role_id]:
            codes_options = (
                autorisation.options_autorisees.split(",")
                if autorisation.options_autorisees
                else []
            )
            libelles_options = ", ".join(
                options_par_code.get(code, f"Option inconnue ({code})")
                for code in codes_options
            )
            if not libelles_options and autorisation.niveau_acces == 0:
                libelles_options = "Aucune option active"

            Habilitations.objects.create(
                audit=audit,
                user_id=affectation.user_id,
                role_id=affectation.role_id,
                code_fonction=autorisation.code_fonction,
                societe=autorisation.societe,
                division=autorisation.division,
                nom_complet=nom_complet,
                nom_role=nom_role,
                libelle_fonction=fonctions.get(
                    autorisation.code_fonction,
                    autorisation.libelle_fonction,
                ),
                statut=autorisation.statut,
                options_autorisees=autorisation.options_autorisees,
                libelles_options_autorisees=libelles_options,
                niveau_acces=autorisation.niveau_acces,
                libelle_niveau_acces=niveaux_acces.get(
                    autorisation.niveau_acces,
                    f"Niveau inconnu ({autorisation.niveau_acces})",
                ),
            )
            nombre_habilitations += 1

    return audit, nombre_habilitations


def write_audit_csv(audit: AuditHabilitations, response) -> None:
    """Écrit l'export CSV d'un audit dans une réponse HTTP ou un fichier."""
    writer = csv.writer(response, delimiter=";")
    writer.writerow(AUDIT_EXPORT_FIELDS)
    for habilitation in audit.habilitations.order_by(
        "user_id", "role_id", "code_fonction", "societe", "division"
    ):
        writer.writerow([getattr(habilitation, field) for field in AUDIT_EXPORT_FIELDS])
