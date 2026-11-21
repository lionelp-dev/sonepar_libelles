from django.core.management.base import BaseCommand

from app.models import LibelleRole
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise les libellés de rôles depuis le CSV"

    def handle(self, *args, **options):
        created, updated = seed_csv(
            filename="libelles_roles.csv",
            model=LibelleRole,
            fields=("code_role", "libelle"),
            lookup_fields=("code_role",),
        )
        self.stdout.write(
            self.style.SUCCESS(f"Libellés de rôles synchronisés ({created} créés, {updated} mis à jour).")
        )
