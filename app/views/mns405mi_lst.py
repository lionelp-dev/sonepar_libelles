"""Vue de consultation de MNS405MI_Lst."""

from rest_framework.decorators import api_view

from ..models import MNS405MI_Lst
from ..serializers import MNS405MI_LstSerializer
from .common import list_response


@api_view(["GET"])
def mns405mi_lst(request):
    return list_response(MNS405MI_Lst.objects.order_by("role_id"), MNS405MI_LstSerializer)
