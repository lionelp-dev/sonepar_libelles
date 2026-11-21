import csv
from datetime import datetime

from django.http import HttpResponse
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


EXPORT_FIELDS = (
    "trdt", "trtm", "usiu", "conu", "divu", "prgnu", "libelle_prgnu",
    "changed_by", "trans_program", "libelle_trans_program", "op_code", "libelle_op_code",
    "changed_role", "libelle_changed_role", "changed_fnc", "libelle_changed_fnc",
    "changed_user", "type_droit", "code_option", "libelle_option", "autorisee_avant",
    "autorisee_apres",
)


def enriched_ses510mi_queryset():
    """Retourne l'audit SES510 avec ses libellés locaux."""
    queryset = with_program_label(SES510MI_Lst.objects.all(), "prgnu", "libelle_prgnu")
    queryset = with_program_label(queryset, "trans_program", "libelle_trans_program")
    queryset = with_function_label(queryset, "changed_fnc", "libelle_changed_fnc")
    queryset = with_role_label(queryset, "changed_role")
    queryset = with_op_code_label(queryset)
    queryset = with_option_label(queryset, "code_option")
    return queryset.order_by(
        "-trdt", "-trtm", "usiu", "conu", "divu", "prgnu", "type_droit", "code_option",
    )


@api_view(["GET"])
def ses510mi_lst(request):
    return list_response(enriched_ses510mi_queryset(), SES510MI_LstSerializer)


@api_view(["GET"])
def export_ses510mi_lst(request):
    """Télécharge l'intégralité de l'audit SES510 enrichi au format CSV."""
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    response["Content-Disposition"] = f'attachment; filename="ses510mi_lst_enrichi_{timestamp}.csv"'

    writer = csv.writer(response, delimiter=";")
    writer.writerow(EXPORT_FIELDS)
    for audit in enriched_ses510mi_queryset().values(*EXPORT_FIELDS).iterator():
        writer.writerow([audit[field] if audit[field] is not None else "" for field in EXPORT_FIELDS])

    return response
