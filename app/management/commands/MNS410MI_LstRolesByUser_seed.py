import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import MNS410MI_LstRolesByUser


class Command(BaseCommand):
    """Seed les associations utilisateur-rôle M3 si la table est vide."""

    help = "Seed les associations utilisateur-rôle M3 si la table est vide"

    def handle(self, *args, **options):
        if MNS410MI_LstRolesByUser.objects.exists():
            self.stdout.write("Des associations utilisateur-rôle M3 existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "MNS410MI_LstRolesByUser.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                MNS410MI_LstRolesByUser.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Associations utilisateur-rôle M3 seedées."))
