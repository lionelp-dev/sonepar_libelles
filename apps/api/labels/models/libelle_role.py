from django.db import models


class LibelleRole(models.Model):
    """Libellé local associé à un code de rôle M3."""

    code_role = models.CharField(max_length=50)
    libelle = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "libelles_roles"
        constraints = [
            models.UniqueConstraint(fields=("code_role",), name="libelle_role_code_unique"),
        ]

    def __str__(self):
        return f"{self.code_role} - {self.libelle}"
