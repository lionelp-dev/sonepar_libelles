from django.db import models


class LibellesFonctions(models.Model):
    """Un libellé de fonction M3."""

    code_fonction = models.CharField(max_length=50, primary_key=True)
    libelle_fonction = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "libelles_fonctions"

    def __str__(self):
        return f"{self.code_fonction} - {self.libelle_fonction}"
