from django.db import models


class LibelleOpCode(models.Model):
    """Libellé local associé à un code opération M3."""

    op_code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "libelles_op_codes"
        constraints = [
            models.UniqueConstraint(fields=("op_code",), name="libelle_op_code_unique"),
        ]

    def __str__(self):
        return f"{self.op_code} - {self.libelle}"
