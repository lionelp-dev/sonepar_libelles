"""Controller REST des libellés d'options."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import LibelleOption
from ..serializers import LibelleOptionSerializer
from ..services.label_management import (
    create_label,
    upsert_label,
)
from .common import paginated_list_response


class OptionLabelViewSet(ViewSet):
    """Controller REST des libellés d'options."""

    lookup_field = "code_option"

    def list(self, request):
        return paginated_list_response(
            LibelleOption.objects.order_by("code_option"),
            LibelleOptionSerializer,
            request,
        )

    def create(self, request):
        serializer = create_label(
            serializer_class=LibelleOptionSerializer,
            data=request.data,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, code_option=None):
        serializer, created = upsert_label(
            code=code_option,
            data=request.data,
            model=LibelleOption,
            serializer_class=LibelleOptionSerializer,
            code_field="code_option",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    def partial_update(self, request, code_option=None):
        serializer, created = upsert_label(
            code=code_option,
            data=request.data,
            model=LibelleOption,
            serializer_class=LibelleOptionSerializer,
            code_field="code_option",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
