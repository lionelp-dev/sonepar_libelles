"""Controller REST des libellés de programmes."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import LibelleProgramme
from ..serializers import LibelleProgrammeSerializer
from ..services.label_management import (
    create_label,
    upsert_label,
)
from .common import paginated_list_response


class ProgramLabelViewSet(ViewSet):
    """Controller REST des libellés de programmes."""

    lookup_field = "code_programme"

    def list(self, request):
        return paginated_list_response(
            LibelleProgramme.objects.order_by("code_programme"),
            LibelleProgrammeSerializer,
            request,
        )

    def create(self, request):
        serializer = create_label(
            serializer_class=LibelleProgrammeSerializer,
            data=request.data,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, code_programme=None):
        serializer, created = upsert_label(
            code=code_programme,
            data=request.data,
            model=LibelleProgramme,
            serializer_class=LibelleProgrammeSerializer,
            code_field="code_programme",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    def partial_update(self, request, code_programme=None):
        serializer, created = upsert_label(
            code=code_programme,
            data=request.data,
            model=LibelleProgramme,
            serializer_class=LibelleProgrammeSerializer,
            code_field="code_programme",
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
