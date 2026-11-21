from django.db import models


class SES510MI_Lst(models.Model):
    """Ligne d'audit de sécurité M3 retournée par SES510MI_Lst."""

    trdt = models.DateField()
    trtm = models.TimeField()
    usiu = models.CharField(max_length=50)
    conu = models.CharField(max_length=20)
    divu = models.CharField(max_length=20)
    prgnu = models.CharField(max_length=50, db_index=True)
    changed_by = models.CharField(max_length=50)
    trans_program = models.CharField(max_length=50, db_index=True)
    op_code = models.CharField(max_length=10, db_index=True)
    changed_role = models.CharField(max_length=50, blank=True, db_index=True)
    changed_fnc = models.CharField(max_length=50, blank=True, db_index=True)
    changed_user = models.CharField(max_length=50, blank=True)
    type_droit = models.CharField(max_length=50)
    code_option = models.CharField(max_length=50, db_index=True)
    autorisee_avant = models.CharField(max_length=10)
    autorisee_apres = models.CharField(max_length=10)

    class Meta:
        db_table = "ses510mi_lst"
        constraints = [
            models.UniqueConstraint(
                fields=("trdt", "trtm", "usiu", "conu", "divu", "prgnu", "type_droit", "code_option"),
                name="ses510mi_audit_unique",
            ),
        ]
