from django.core.management.base import BaseCommand

from app.models import LibelleOption
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les libellés d'options depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="libelles_options.csv",
            model=LibelleOption,
            fields=("code_option", "libelle"),
            lookup_fields=("code_option",),
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Libellés d'options synchronisés ({created} créés, {updated} mis à jour)."
            )
        )
