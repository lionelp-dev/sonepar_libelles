"""Annotations ORM pour enrichir les sources M3 avec leurs libellés locaux."""

from django.db.models import CharField, OuterRef, Subquery
from django.db.models.functions import Cast

from app.models import LibelleFonction, LibelleOpCode, LibelleOption, LibelleProgramme, LibelleRole


def with_function_label(queryset, source_field: str, annotation: str):
    return queryset.annotate(
        **{
            annotation: Subquery(
                LibelleFonction.objects.filter(code_fonction=OuterRef(source_field)).values("libelle")[:1],
                output_field=CharField(),
            ),
        },
    )


def with_option_label(queryset, source_field: str, annotation: str = "libelle_option"):
    return queryset.annotate(
        **{
            annotation: Subquery(
                LibelleOption.objects.filter(
                    code_option=Cast(OuterRef(source_field), output_field=CharField()),
                ).values("libelle")[:1],
                output_field=CharField(),
            ),
        },
    )


def with_role_label(queryset, source_field: str, annotation: str = "libelle_changed_role"):
    return queryset.annotate(
        **{
            annotation: Subquery(
                LibelleRole.objects.filter(code_role=OuterRef(source_field)).values("libelle")[:1],
                output_field=CharField(),
            ),
        },
    )


def with_program_label(queryset, source_field: str, annotation: str):
    return queryset.annotate(
        **{
            annotation: Subquery(
                LibelleProgramme.objects.filter(code_programme=OuterRef(source_field)).values("libelle")[:1],
                output_field=CharField(),
            ),
        },
    )


def with_op_code_label(queryset, source_field: str = "op_code", annotation: str = "libelle_op_code"):
    return queryset.annotate(
        **{
            annotation: Subquery(
                LibelleOpCode.objects.filter(op_code=OuterRef(source_field)).values("libelle")[:1],
                output_field=CharField(),
            ),
        },
    )
