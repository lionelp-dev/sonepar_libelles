"""Vue de consultation de LibellesFonctions."""

from rest_framework.decorators import api_view

from ..models import LibellesFonctions
from ..serializers import LibellesFonctionsSerializer
from .common import list_response


@api_view(["GET"])
def libelles_fonctions(request):
    return list_response(
        LibellesFonctions.objects.order_by("code_fonction"),
        LibellesFonctionsSerializer,
    )
