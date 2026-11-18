from rest_framework.decorators import api_view

from ..models import Habilitations
from ..serializers import HabilitationsSerializer
from .common import list_response


@api_view(["GET"])
def habilitations(request):
    return list_response(
        Habilitations.objects.order_by("-audit_id", "user_id", "role_id", "code_fonction"),
        HabilitationsSerializer,
    )
