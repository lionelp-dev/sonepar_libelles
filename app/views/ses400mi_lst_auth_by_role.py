"""Vue de consultation de SES400MI_LstAuthByRole."""

from rest_framework.decorators import api_view

from ..models import SES400MI_LstAuthByRole
from ..serializers import SES400MI_LstAuthByRoleSerializer
from .common import list_response


@api_view(["GET"])
def ses400mi_lst_auth_by_role(request):
    return list_response(
        SES400MI_LstAuthByRole.objects.order_by(
            "role_id",
            "code_fonction",
            "societe",
            "division",
            "code_option",
        ),
        SES400MI_LstAuthByRoleSerializer,
    )
