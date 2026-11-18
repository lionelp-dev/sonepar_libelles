import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import SES400MI_LstAuthByRole


class Command(BaseCommand):
    """Seed les autorisations de rôle M3 si la table est vide."""

    help = "Seed les autorisations de rôle M3 si la table est vide"

    def handle(self, *args, **options):
        if SES400MI_LstAuthByRole.objects.exists():
            self.stdout.write("Des autorisations de rôle M3 existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "SES400MI_LstAuthByRole.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                SES400MI_LstAuthByRole.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Autorisations de rôle M3 seedées."))
