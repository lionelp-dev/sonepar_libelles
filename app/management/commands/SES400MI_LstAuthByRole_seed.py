from django.core.management.base import BaseCommand

from app.models import SES400MI_LstAuthByRole
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les autorisations de rôle M3 depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="SES400MI_LstAuthByRole.csv",
            model=SES400MI_LstAuthByRole,
            fields=(
                "role_id", "code_fonction", "libelle_fonction", "societe", "division", "statut", "code_option",
            ),
            lookup_fields=("role_id", "code_fonction", "societe", "division", "code_option"),
        )
        self.stdout.write(self.style.SUCCESS(f"Autorisations de rôle synchronisées ({created} créées, {updated} mises à jour)."))
