"""Synchronisation des catalogues de libellés à partir de l'audit SES510."""

from collections.abc import Iterable

from app.models import (
    LibelleFonction,
    LibelleOpCode,
    LibelleOption,
    LibelleProgramme,
    LibelleRole,
    SES510MI_Lst,
)


def _create_missing(model, code_field: str, codes: Iterable[str]) -> None:
    """Insère les codes absents par lots, sans toucher aux libellés existants."""
    batch = []
    for code in codes:
        batch.append(model(**{code_field: code, "libelle": None}))
        if len(batch) == 1_000:
            model.objects.bulk_create(batch, ignore_conflicts=True)
            batch.clear()
    if batch:
        model.objects.bulk_create(batch, ignore_conflicts=True)


def synchronize_label_catalogs() -> None:
    """Ajoute aux catalogues les codes distincts présents dans SES510."""
    audits = SES510MI_Lst.objects

    _create_missing(
        LibelleFonction,
        "code_fonction",
        audits.exclude(changed_fnc="").values_list("changed_fnc", flat=True).distinct().iterator(),
    )
    _create_missing(
        LibelleProgramme,
        "code_programme",
        audits.exclude(prgnu="").values_list("prgnu", flat=True).union(
            audits.exclude(trans_program="").values_list("trans_program", flat=True),
        ).iterator(),
    )
    _create_missing(
        LibelleRole,
        "code_role",
        audits.exclude(changed_role="").values_list("changed_role", flat=True).distinct().iterator(),
    )
    _create_missing(
        LibelleOption,
        "code_option",
        audits.exclude(code_option="").values_list("code_option", flat=True).distinct().iterator(),
    )
    _create_missing(
        LibelleOpCode,
        "op_code",
        audits.exclude(op_code="").values_list("op_code", flat=True).distinct().iterator(),
    )
