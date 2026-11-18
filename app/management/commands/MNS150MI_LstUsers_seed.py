import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import MNS150MI_LstUsers


class Command(BaseCommand):
    """Seed les utilisateurs M3 si la table est vide."""

    help = "Seed les utilisateurs M3 si la table est vide"

    def handle(self, *args, **options):
        if MNS150MI_LstUsers.objects.exists():
            self.stdout.write("Des utilisateurs M3 existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "MNS150MI_LstUsers.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                MNS150MI_LstUsers.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Utilisateurs M3 seedés."))
