"""Controller REST des libellés de codes opération."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import LibelleOpCode
from ..serializers import LibelleOpCodeSerializer
from ..services.label_management import (
    create_label,
    upsert_label,
)
from .common import paginated_list_response


class OpCodeLabelViewSet(ViewSet):
    """Controller REST des libellés de codes opération."""

    lookup_field = "op_code"

    def list(self, request):
        return paginated_list_response(
            LibelleOpCode.objects.order_by("op_code"),
            LibelleOpCodeSerializer,
            request,
        )

    def create(self, request):
        serializer = create_label(
            serializer_class=LibelleOpCodeSerializer,
            data=request.data,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, op_code=None):
        serializer, created = upsert_label(
            code=op_code,
            data=request.data,
            model=LibelleOpCode,
            serializer_class=LibelleOpCodeSerializer,
            code_field="op_code",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    def partial_update(self, request, op_code=None):
        serializer, created = upsert_label(
            code=op_code,
            data=request.data,
            model=LibelleOpCode,
            serializer_class=LibelleOpCodeSerializer,
            code_field="op_code",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
