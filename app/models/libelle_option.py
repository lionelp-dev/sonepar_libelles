from django.db import models


class LibelleOption(models.Model):
    """Libellé local associé à un code d'option M3."""

    code_option = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "libelles_options"
        constraints = [
            models.UniqueConstraint(fields=("code_option",), name="libelle_option_code_unique"),
        ]

    def __str__(self):
        return f"{self.code_option} - {self.libelle}"
