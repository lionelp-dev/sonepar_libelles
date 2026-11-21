from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("function-labels", views.FunctionLabelViewSet, basename="function-label")
router.register("option-labels", views.OptionLabelViewSet, basename="option-label")
router.register("program-labels", views.ProgramLabelViewSet, basename="program-label")
router.register("role-labels", views.RoleLabelViewSet, basename="role-label")
router.register("op-code-labels", views.OpCodeLabelViewSet, basename="op-code-label")


urlpatterns = [
    path("health/", views.health),
    path("", include(router.urls)),
    path("ses510mi/export/", views.export_ses510mi_lst),
    path("ses510mi/", views.ses510mi_lst),
]
