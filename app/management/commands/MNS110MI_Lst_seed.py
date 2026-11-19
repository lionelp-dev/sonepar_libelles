from django.core.management.base import BaseCommand

from app.models import MNS110MI_Lst
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise MNS110MI_Lst depuis le CSV"

    def handle(self, *args, **options):
        def transform(row):
            if row["autorisation_requise"] not in {"0", "1"}:
                raise ValueError("autorisation_requise doit valoir 0 ou 1")
            return row

        created, updated = seed_csv(
            filename="MNS110MI_Lst.csv",
            model=MNS110MI_Lst,
            fields=("code_fonction", "programme_m3", "categorie_fonction", "autorisation_requise"),
            lookup_fields=("code_fonction",),
            transform=transform,
        )
        self.stdout.write(self.style.SUCCESS(f"Catalogue de fonctions synchronisé ({created} créées, {updated} mises à jour)."))
