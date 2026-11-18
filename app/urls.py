from django.urls import path

from . import views


urlpatterns = [
    path("health/", views.health),
    path("users/", views.mns150mi_lst_users),
    path("roles/", views.mns405mi_lst),
    path("user-role-assignments/", views.mns410mi_lst_roles_by_user),
    path("role-authorizations/", views.ses400mi_lst_auth_by_role),
    path("function-labels/", views.libelles_fonctions),
    path("access-levels/", views.libelles_niveaux_acces),
    path("options/", views.libelles_options),
    path("audits/", views.audit_habilitations),
    path("audits/<int:audit_id>/export/", views.export_audit_habilitations),
    path("habilitations/", views.habilitations),
]
