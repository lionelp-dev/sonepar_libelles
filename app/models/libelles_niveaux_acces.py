from django.db import models


class LibellesNiveauxAcces(models.Model):
    """Un libellé de niveau d'accès."""

    niveau_acces = models.PositiveSmallIntegerField(primary_key=True)
    libelle_niveau_acces = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "libelles_niveaux_acces"

    def __str__(self):
        return f"{self.niveau_acces} - {self.libelle_niveau_acces}"
