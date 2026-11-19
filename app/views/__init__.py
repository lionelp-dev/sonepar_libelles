"""Vues HTTP organisées par source de données M3."""

from .health import health
from .libelles_fonctions import libelles_fonctions
from .libelles_options import libelles_options
from .mns110mi_lst import mns110mi_lst
from .mns150mi_lst_users import mns150mi_lst_users
from .mns405mi_lst import mns405mi_lst
from .mns410mi_lst_roles_by_user import mns410mi_lst_roles_by_user
from .ses400mi_lst_auth_by_role import ses400mi_lst_auth_by_role
from .ses401_cmpnus import ses401_cmpnus
from .ses510mi_lst import ses510mi_lst

__all__ = [
    "health",
    "libelles_fonctions",
    "libelles_options",
    "mns110mi_lst",
    "mns150mi_lst_users",
    "mns405mi_lst",
    "mns410mi_lst_roles_by_user",
    "ses400mi_lst_auth_by_role",
    "ses401_cmpnus",
    "ses510mi_lst",
]
