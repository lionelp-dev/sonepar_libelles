from django.db import models


class LibelleFonction(models.Model):
    """Libellé local associé à un code de fonction ou de programme M3."""

    code_fonction = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "libelles_fonctions"
        constraints = [
            models.UniqueConstraint(fields=("code_fonction",), name="libelle_fonction_code_unique"),
        ]

    def __str__(self):
        return f"{self.code_fonction} - {self.libelle}"
