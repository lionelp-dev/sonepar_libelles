from django.db import models


class MNS150MI_LstUsers(models.Model):
    """Un utilisateur retourné par MNS150MI_LstUsers."""

    user_id = models.CharField(max_length=50, primary_key=True)
    nom_complet = models.CharField(max_length=255)
    statut = models.CharField(max_length=10)

    class Meta:
        db_table = "mns150mi_lst_users"

    def __str__(self):
        return self.nom_complet
