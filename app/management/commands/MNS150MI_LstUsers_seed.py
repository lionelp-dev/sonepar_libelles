from django.core.management.base import BaseCommand

from app.models import MNS150MI_LstUsers
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les utilisateurs M3 depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="MNS150MI_LstUsers.csv",
            model=MNS150MI_LstUsers,
            fields=("user_id", "nom_complet", "statut"),
            lookup_fields=("user_id",),
        )
        self.stdout.write(self.style.SUCCESS(f"Utilisateurs M3 synchronisés ({created} créés, {updated} mis à jour)."))
