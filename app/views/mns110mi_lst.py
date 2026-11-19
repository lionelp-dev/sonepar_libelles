"""Vue de consultation de MNS110MI_Lst."""

from rest_framework.decorators import api_view

from ..models import MNS110MI_Lst
from ..serializers import MNS110MI_LstSerializer
from .common import list_response


@api_view(["GET"])
def mns110mi_lst(request):
    return list_response(
        MNS110MI_Lst.objects.order_by("code_fonction"),
        MNS110MI_LstSerializer,
    )
