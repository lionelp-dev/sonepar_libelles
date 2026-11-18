"""Vue de consultation de MNS150MI_LstUsers."""

from rest_framework.decorators import api_view

from ..models import MNS150MI_LstUsers
from ..serializers import MNS150MI_LstUsersSerializer
from .common import list_response


@api_view(["GET"])
def mns150mi_lst_users(request):
    return list_response(MNS150MI_LstUsers.objects.order_by("user_id"), MNS150MI_LstUsersSerializer)
