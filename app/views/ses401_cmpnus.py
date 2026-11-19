"""Vue de consultation de SES401_CMNPUS."""

from rest_framework.decorators import api_view

from ..models import SES401_CMNPUS
from ..serializers import SES401_CMNPUSSerializer
from .common import list_response


@api_view(["GET"])
def ses401_cmpnus(request):
    return list_response(
        SES401_CMNPUS.objects.order_by(
            "user_id", "programme_m3", "societe", "division", "role_id", "code_option"
        ),
        SES401_CMNPUSSerializer,
    )
