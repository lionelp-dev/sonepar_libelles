import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import LibellesOptions


class Command(BaseCommand):
    """Seed les libellés d'options si la table est vide."""

    help = "Seed les libellés d'options si la table est vide"

    def handle(self, *args, **options):
        if LibellesOptions.objects.exists():
            self.stdout.write("Des libellés d'options existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "libelles_options.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                LibellesOptions.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Libellés d'options seedés."))
