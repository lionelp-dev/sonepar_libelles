from django.db import models


class SES510MI_Lst(models.Model):
    """Une entrée du journal des modifications d'habilitations SES510."""

    id_evenement = models.CharField(max_length=50)
    trdt = models.DateField()
    trtm = models.TimeField()
    usiu = models.CharField(max_length=50)
    conu = models.CharField(max_length=20)
    divu = models.CharField(max_length=20)
    prgnu = models.CharField(max_length=50)
    modifie_par = models.CharField(max_length=50)
    programme_origine = models.CharField(max_length=50)
    code_operation = models.CharField(max_length=10)
    role_modifie = models.CharField(max_length=50, blank=True)
    fonction_modifiee = models.CharField(max_length=50, blank=True)
    utilisateur_modifie = models.CharField(max_length=50, blank=True)
    code_option = models.CharField(max_length=10, blank=True)
    autorisee_avant = models.CharField(max_length=10)
    autorisee_apres = models.CharField(max_length=10)
    options_de_base_modifiees = models.CharField(max_length=10, blank=True)
    options_associees_modifiees = models.CharField(max_length=10, blank=True)
    touches_fonction_modifiees = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = "ses510mi_lst"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "id_evenement",
                    "code_option",
                ],
                name="ses510_evenement_option_unique",
            ),
        ]

    def __str__(self):
        return f"{self.id_evenement} - option {self.code_option}"
