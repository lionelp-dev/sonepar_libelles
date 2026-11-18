"""Vue de consultation de LibellesNiveauxAcces."""

from rest_framework.decorators import api_view

from ..models import LibellesNiveauxAcces
from ..serializers import LibellesNiveauxAccesSerializer
from .common import list_response


@api_view(["GET"])
def libelles_niveaux_acces(request):
    return list_response(
        LibellesNiveauxAcces.objects.order_by("niveau_acces"),
        LibellesNiveauxAccesSerializer,
    )
