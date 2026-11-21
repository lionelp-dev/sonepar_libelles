from rest_framework.decorators import api_view

from ..models import SES510MI_Lst
from ..serializers import SES510MI_LstSerializer
from ..services.label_enrichment import (
    with_function_label,
    with_op_code_label,
    with_option_label,
    with_program_label,
    with_role_label,
)
from .common import list_response


@api_view(["GET"])
def ses510mi_lst(request):
    queryset = with_program_label(SES510MI_Lst.objects.all(), "prgnu", "libelle_prgnu")
    queryset = with_program_label(queryset, "trans_program", "libelle_trans_program")
    queryset = with_function_label(queryset, "changed_fnc", "libelle_changed_fnc")
    queryset = with_role_label(queryset, "changed_role")
    queryset = with_op_code_label(queryset)
    queryset = with_option_label(queryset, "code_option")
    return list_response(
        queryset.order_by("-trdt", "-trtm", "usiu", "conu", "divu", "prgnu", "type_droit", "code_option"),
        SES510MI_LstSerializer,
    )
