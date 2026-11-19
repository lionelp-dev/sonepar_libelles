from django.core.management.base import BaseCommand

from app.models import MNS410MI_LstRolesByUser
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les associations utilisateur-rôle M3 depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="MNS410MI_LstRolesByUser.csv",
            model=MNS410MI_LstRolesByUser,
            fields=("user_id", "role_id"),
            lookup_fields=("user_id", "role_id"),
        )
        self.stdout.write(self.style.SUCCESS(f"Associations utilisateur-rôle synchronisées ({created} créées, {updated} mises à jour)."))
