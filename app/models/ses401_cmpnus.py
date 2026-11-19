from django.db import models


class SES401_CMNPUS(models.Model):
    """Un droit effectif par utilisateur retourné par SES401."""

    user_id = models.CharField(max_length=50)
    nom_complet = models.CharField(max_length=255)
    programme_m3 = models.CharField(max_length=50)
    societe = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    role_id = models.CharField(max_length=50)
    code_option = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = "ses401_cmpnus"
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "programme_m3", "societe", "division", "role_id", "code_option"],
                name="ses401_user_programme_role_option_unique",
            ),
        ]

    def __str__(self):
        return f"{self.user_id} - {self.programme_m3}"
