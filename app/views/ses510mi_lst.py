"""Vue de consultation de SES510MI_Lst."""

from rest_framework.decorators import api_view

from ..models import SES510MI_Lst
from ..serializers import SES510MI_LstSerializer
from .common import list_response


@api_view(["GET"])
def ses510mi_lst(request):
    return list_response(
        SES510MI_Lst.objects.order_by("-trdt", "-trtm", "id_evenement", "code_option"),
        SES510MI_LstSerializer,
    )
