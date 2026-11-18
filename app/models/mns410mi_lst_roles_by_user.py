from django.db import models


class MNS410MI_LstRolesByUser(models.Model):
    """Une affectation de rôle à un utilisateur retournée par MNS410MI."""

    user_id = models.CharField(max_length=50)
    role_id = models.CharField(max_length=50)

    class Meta:
        db_table = "mns410mi_lst_roles_by_user"
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "role_id"],
                name="mns410mi_user_role_unique",
            ),
        ]

    def __str__(self):
        return f"{self.user_id} - {self.role_id}"
