"""Vue de consultation de LibellesOptions."""

from rest_framework.decorators import api_view

from ..models import LibellesOptions
from ..serializers import LibellesOptionsSerializer
from .common import list_response


@api_view(["GET"])
def libelles_options(request):
    return list_response(LibellesOptions.objects.order_by("code_option"), LibellesOptionsSerializer)
