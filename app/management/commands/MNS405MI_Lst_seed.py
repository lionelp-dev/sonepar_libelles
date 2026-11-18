import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import MNS405MI_Lst


class Command(BaseCommand):
    """Seed les rôles M3 si la table est vide."""

    help = "Seed les rôles M3 si la table est vide"

    def handle(self, *args, **options):
        if MNS405MI_Lst.objects.exists():
            self.stdout.write("Des rôles M3 existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "MNS405MI_Lst.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                MNS405MI_Lst.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Rôles M3 seedés."))
