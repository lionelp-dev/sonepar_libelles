from collections import defaultdict

from django.core.management.base import BaseCommand

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


class Command(BaseCommand):
    """Affiche l'audit des habilitations M3."""

    help = "Affiche l'audit des habilitations M3 dans le terminal"

    def handle(self, *args, **options):
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

        self.stdout.write(f"AUDIT DES HABILITATIONS #{audit.pk} - {audit.created_at.isoformat()}")
        self.stdout.write(
            "Utilisateur | Rôle | Fonction | Société | Division | Statut | Options | Niveau d'accès"
        )
        self.stdout.write("-" * 120)

        nombre_habilitations = 0
        for affectation in MNS410MI_LstRolesByUser.objects.order_by("user_id", "role_id"):
            nom_complet = utilisateurs.get(
                affectation.user_id,
                f"Utilisateur inconnu ({affectation.user_id})",
            )
            nom_role = roles.get(affectation.role_id, f"Rôle inconnu ({affectation.role_id})")

            for autorisation in autorisations_par_role[affectation.role_id]:
                codes_options = autorisation.options_autorisees.split(",") if autorisation.options_autorisees else []
                libelles_options = ", ".join(
                    options_par_code.get(code, f"Option inconnue ({code})")
                    for code in codes_options
                )
                if not libelles_options and autorisation.niveau_acces == 0:
                    libelles_options = "Aucune option active"

                libelle_fonction = fonctions.get(
                    autorisation.code_fonction,
                    autorisation.libelle_fonction,
                )
                libelle_niveau = niveaux_acces.get(
                    autorisation.niveau_acces,
                    f"Niveau inconnu ({autorisation.niveau_acces})",
                )

                habilitation = Habilitations.objects.create(
                    audit=audit,
                    user_id=affectation.user_id,
                    role_id=affectation.role_id,
                    code_fonction=autorisation.code_fonction,
                    societe=autorisation.societe,
                    division=autorisation.division,
                    nom_complet=nom_complet,
                    nom_role=nom_role,
                    libelle_fonction=libelle_fonction,
                    statut=autorisation.statut,
                    options_autorisees=autorisation.options_autorisees,
                    libelles_options_autorisees=libelles_options,
                    niveau_acces=autorisation.niveau_acces,
                    libelle_niveau_acces=libelle_niveau,
                )

                self.stdout.write(
                    f"{habilitation.user_id} - {habilitation.nom_complet} | "
                    f"{habilitation.role_id} - {habilitation.nom_role} | "
                    f"{habilitation.code_fonction} - {habilitation.libelle_fonction} | "
                    f"{habilitation.societe} | {habilitation.division} | {habilitation.statut} | "
                    f"{habilitation.libelles_options_autorisees or '-'} | "
                    f"{habilitation.niveau_acces} - {habilitation.libelle_niveau_acces}"
                )
                nombre_habilitations += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Audit #{audit.pk} : {nombre_habilitations} habilitation(s) générée(s) et affichée(s)."
            )
        )
