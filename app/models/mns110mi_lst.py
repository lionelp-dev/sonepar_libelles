from django.db import models


class MNS110MI_Lst(models.Model):
    """Une fonction M3 retournée par MNS110MI_Lst."""

    code_fonction = models.CharField(max_length=50, primary_key=True)
    programme_m3 = models.CharField(max_length=50)
    categorie_fonction = models.CharField(max_length=20)
    autorisation_requise = models.CharField(max_length=1)

    class Meta:
        db_table = "mns110mi_lst"

    def __str__(self):
        return f"{self.code_fonction} - {self.programme_m3}"
