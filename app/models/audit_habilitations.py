from django.db import models


class AuditHabilitations(models.Model):
    """Un audit horodaté des habilitations M3."""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "audit_habilitations"

    def __str__(self):
        return self.created_at.isoformat()
