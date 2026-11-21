"""Controller REST des libellés de fonctions."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import LibelleFonction
from ..serializers import LibelleFonctionSerializer
from ..services.label_management import (
    create_label,
    upsert_label,
)
from .common import paginated_list_response


class FunctionLabelViewSet(ViewSet):
    """Controller REST des libellés de fonctions."""

    lookup_field = "code_fonction"

    def list(self, request):
        return paginated_list_response(
            LibelleFonction.objects.order_by("code_fonction"),
            LibelleFonctionSerializer,
            request,
        )

    def create(self, request):
        serializer = create_label(
            serializer_class=LibelleFonctionSerializer,
            data=request.data,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, code_fonction=None):
        serializer, created = upsert_label(
            code=code_fonction,
            data=request.data,
            model=LibelleFonction,
            serializer_class=LibelleFonctionSerializer,
            code_field="code_fonction",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    def partial_update(self, request, code_fonction=None):
        serializer, created = upsert_label(
            code=code_fonction,
            data=request.data,
            model=LibelleFonction,
            serializer_class=LibelleFonctionSerializer,
            code_field="code_fonction",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
