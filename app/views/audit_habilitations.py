"""Vues de création, consultation et export de AuditHabilitations."""

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import AuditHabilitations
from ..serializers import AuditHabilitationsSerializer, HabilitationsSerializer
from ..services.audit_habilitations import generate_audit, write_audit_csv
from .common import list_response


def audits_queryset():
    return AuditHabilitations.objects.annotate(habilitations_count=Count("habilitations"))


@api_view(["GET", "POST"])
def audit_habilitations(request):
    if request.method == "POST":
        audit, _ = generate_audit()
        audit = audits_queryset().get(pk=audit.pk)
        return Response(AuditHabilitationsSerializer(audit).data, status=status.HTTP_201_CREATED)

    return list_response(
        audits_queryset().order_by("-created_at", "-pk"),
        AuditHabilitationsSerializer,
    )


@api_view(["GET"])
def audit_habilitation_detail(request, audit_id):
    """Retourne les métadonnées d'un instantané d'audit."""
    audit = get_object_or_404(audits_queryset(), pk=audit_id)
    return Response(AuditHabilitationsSerializer(audit).data)


@api_view(["GET"])
def audit_habilitation_habilitations(request, audit_id):
    """Retourne uniquement les lignes de l'instantané demandé."""
    audit = get_object_or_404(AuditHabilitations, pk=audit_id)
    return list_response(
        audit.habilitations.order_by(
            "user_id", "role_id", "code_fonction", "societe", "division"
        ),
        HabilitationsSerializer,
    )


@api_view(["GET"])
def export_audit_habilitations(request, audit_id):
    audit = get_object_or_404(AuditHabilitations, pk=audit_id)
    date_audit = audit.created_at.strftime("%Y%m%d_%H%M%S")
    filename = f"audit_habilitations_{audit.pk}_{date_audit}.csv"
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    response.write("\ufeff")
    write_audit_csv(audit, response)
    return response
