from django.db import models


class LibellesOptions(models.Model):
    """Un libellé d'option M3."""

    code_option = models.PositiveSmallIntegerField(primary_key=True)
    libelle_option = models.CharField(max_length=255)
    libelle_anglais = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "libelles_options"

    def __str__(self):
        return f"{self.code_option} - {self.libelle_option}"
