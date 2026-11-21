from django.core.management.base import BaseCommand

from app.models import LibelleFonction
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les libellés de fonctions depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="libelles_fonctions.csv",
            model=LibelleFonction,
            fields=("code_fonction", "libelle"),
            lookup_fields=("code_fonction",),
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Libellés de fonctions synchronisés ({created} créés, {updated} mis à jour)."
            )
        )
