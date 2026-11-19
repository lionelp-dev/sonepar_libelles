from django.urls import path

from . import views


urlpatterns = [
    path("health/", views.health),
    path("function-catalog/", views.mns110mi_lst),
    path("users/", views.mns150mi_lst_users),
    path("roles/", views.mns405mi_lst),
    path("user-role-assignments/", views.mns410mi_lst_roles_by_user),
    path("role-authorizations/", views.ses400mi_lst_auth_by_role),
    path("user-authorizations/", views.ses401_cmpnus),
    path("authorization-history/", views.ses510mi_lst),
    path("function-labels/", views.libelles_fonctions),
    path("options/", views.libelles_options),
]
