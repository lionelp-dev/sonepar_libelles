from django.db import models


class MNS405MI_Lst(models.Model):
    """Un rôle retourné par MNS405MI_Lst."""

    role_id = models.CharField(max_length=50, primary_key=True)
    nom_role = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = "mns405mi_lst"

    def __str__(self):
        return f"{self.role_id} - {self.nom_role}"
