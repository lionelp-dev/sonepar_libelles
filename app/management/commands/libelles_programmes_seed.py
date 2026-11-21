from django.core.management.base import BaseCommand

from app.models import LibelleProgramme
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les libellés de programmes depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="libelles_programmes.csv",
            model=LibelleProgramme,
            fields=("code_programme", "libelle"),
            lookup_fields=("code_programme",),
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Libellés de programmes synchronisés ({created} créés, {updated} mis à jour)."
            )
        )
