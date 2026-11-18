"""Vue de consultation de MNS410MI_LstRolesByUser."""

from rest_framework.decorators import api_view

from ..models import MNS410MI_LstRolesByUser
from ..serializers import MNS410MI_LstRolesByUserSerializer
from .common import list_response


@api_view(["GET"])
def mns410mi_lst_roles_by_user(request):
    return list_response(
        MNS410MI_LstRolesByUser.objects.order_by("user_id", "role_id"),
        MNS410MI_LstRolesByUserSerializer,
    )
