import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app.models import LibellesNiveauxAcces


class Command(BaseCommand):
    """Seed les libellés de niveaux d'accès si la table est vide."""

    help = "Seed les libellés de niveaux d'accès si la table est vide"

    def handle(self, *args, **options):
        if LibellesNiveauxAcces.objects.exists():
            self.stdout.write("Des libellés de niveaux d'accès existent déjà, aucun seed effectué.")
            return

        fichier_csv = Path(settings.BASE_DIR) / "donnees" / "libelles_niveaux_acces.csv"

        with fichier_csv.open(encoding="utf-8-sig", newline="") as fichier:
            for ligne in csv.DictReader(fichier, delimiter=";"):
                LibellesNiveauxAcces.objects.create(**ligne)

        self.stdout.write(self.style.SUCCESS("Libellés de niveaux d'accès seedés."))
