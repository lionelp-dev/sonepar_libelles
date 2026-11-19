from django.core.management.base import BaseCommand

from app.models import MNS405MI_Lst
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les rôles M3 depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="MNS405MI_Lst.csv",
            model=MNS405MI_Lst,
            fields=("role_id", "nom_role", "description"),
            lookup_fields=("role_id",),
        )
        self.stdout.write(self.style.SUCCESS(f"Rôles M3 synchronisés ({created} créés, {updated} mis à jour)."))
