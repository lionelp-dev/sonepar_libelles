import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import LibellesFonctions


class Command(BaseCommand):
    """Seed les libellés de fonctions si la table est vide."""

    help = "Seed les libellés de fonctions si la table est vide"

    def handle(self, *args, **options):
        if LibellesFonctions.objects.exists():
            self.stdout.write("Des libellés de fonctions existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "libelles_fonctions.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                LibellesFonctions.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Libellés de fonctions seedés."))
