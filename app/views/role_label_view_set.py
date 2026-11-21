"""Controller REST des libellés de rôles."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import LibelleRole
from ..serializers import LibelleRoleSerializer
from ..services.label_management import create_label, upsert_label
from .common import paginated_list_response


class RoleLabelViewSet(ViewSet):
    """Controller REST des libellés de rôles."""

    lookup_field = "code_role"

    def list(self, request):
        return paginated_list_response(
            LibelleRole.objects.order_by("code_role"),
            LibelleRoleSerializer,
            request,
        )

    def create(self, request):
        serializer = create_label(serializer_class=LibelleRoleSerializer, data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, code_role=None):
        serializer, created = upsert_label(
            code=code_role,
            data=request.data,
            model=LibelleRole,
            serializer_class=LibelleRoleSerializer,
            code_field="code_role",
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def partial_update(self, request, code_role=None):
        return self.update(request, code_role)
