from django.db import models


class LibelleProgramme(models.Model):
    """Libellé local associé à un code de programme M3."""

    code_programme = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "libelles_programmes"
        constraints = [
            models.UniqueConstraint(fields=("code_programme",), name="libelle_programme_code_unique"),
        ]

    def __str__(self):
        return f"{self.code_programme} - {self.libelle}"
