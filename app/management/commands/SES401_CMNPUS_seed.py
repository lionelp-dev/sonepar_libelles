from django.core.management.base import BaseCommand

from app.models import SES401_CMNPUS
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise SES401_CMNPUS depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="SES401_CMNPUS.csv",
            model=SES401_CMNPUS,
            fields=(
                "user_id", "nom_complet", "programme_m3", "societe", "division", "role_id", "code_option",
            ),
            lookup_fields=("user_id", "programme_m3", "societe", "division", "role_id", "code_option"),
        )
        self.stdout.write(self.style.SUCCESS(f"Droits effectifs synchronisés ({created} créés, {updated} mis à jour)."))
