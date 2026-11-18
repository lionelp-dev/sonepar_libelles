from django.db import models

from .audit_habilitations import AuditHabilitations


class Habilitations(models.Model):
    """Une ligne de l'export d'habilitations."""

    audit = models.ForeignKey(AuditHabilitations, on_delete=models.CASCADE, related_name="habilitations")
    user_id = models.CharField(max_length=50)
    nom_complet = models.CharField(max_length=255)
    role_id = models.CharField(max_length=50)
    nom_role = models.CharField(max_length=255)
    code_fonction = models.CharField(max_length=50)
    libelle_fonction = models.CharField(max_length=255)
    societe = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    statut = models.CharField(max_length=10)
    options_autorisees = models.CharField(max_length=255)
    libelles_options_autorisees = models.CharField(max_length=255)
    niveau_acces = models.PositiveSmallIntegerField()
    libelle_niveau_acces = models.CharField(max_length=255)

    class Meta:
        db_table = "habilitations"
        constraints = [
            models.UniqueConstraint(
                fields=["audit", "user_id", "role_id", "code_fonction", "societe", "division"],
                name="habilitation_audit_unique",
            ),
        ]

    def __str__(self):
        return f"{self.user_id} - {self.code_fonction}"
