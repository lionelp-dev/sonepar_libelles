from django.core.management.base import BaseCommand

from app.models import LibelleOpCode
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les libellés de codes opération depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="libelles_op_codes.csv",
            model=LibelleOpCode,
            fields=("op_code", "libelle"),
            lookup_fields=("op_code",),
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Libellés de codes opération synchronisés ({created} créés, {updated} mis à jour)."
            )
        )
