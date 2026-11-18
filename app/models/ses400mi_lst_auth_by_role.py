from django.db import models


class SES400MI_LstAuthByRole(models.Model):
    """Une autorisation de rôle retournée par SES400MI."""

    role_id = models.CharField(max_length=50)
    code_fonction = models.CharField(max_length=50)
    libelle_fonction = models.CharField(max_length=255)
    societe = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    statut = models.CharField(max_length=10)
    options_autorisees = models.CharField(max_length=255)
    niveau_acces = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "ses400mi_lst_auth_by_role"
        constraints = [
            models.UniqueConstraint(
                fields=["role_id", "code_fonction", "societe", "division"],
                name="ses400mi_role_fonction_unique",
            ),
        ]

    def __str__(self):
        return f"{self.role_id} - {self.code_fonction}"
