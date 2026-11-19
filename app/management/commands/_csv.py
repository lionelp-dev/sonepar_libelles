"""Utilitaires communs aux commandes d'import des données CSV M3."""

import csv
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path
from typing import Any

from django.conf import settings
from django.core.management.base import CommandError
from django.db import transaction


def seed_csv(
    *,
    filename: str,
    model: Any,
    fields: Iterable[str],
    lookup_fields: Iterable[str],
    transform: Callable[[dict[str, str]], Mapping[str, Any]] | None = None,
) -> tuple[int, int]:
    """Synchronise un CSV local dans un modèle à partir de sa clé métier."""
    expected_fields = tuple(fields)
    source_path = Path(settings.BASE_DIR) / "donnees" / filename
    if not source_path.is_file():
        raise CommandError(f"Fichier CSV introuvable : {source_path}")

    created = 0
    updated = 0
    with source_path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter=";")
        actual_fields = tuple(reader.fieldnames or ())
        if actual_fields != expected_fields:
            raise CommandError(
                f"Colonnes invalides dans {filename}. "
                f"Attendu : {', '.join(expected_fields)}. "
                f"Reçu : {', '.join(actual_fields) or 'aucune'}.",
            )

        with transaction.atomic():
            for number, source_row in enumerate(reader, start=2):
                if None in source_row:
                    raise CommandError(f"Trop de colonnes dans {filename}, ligne {number}.")
                try:
                    row = dict(transform(source_row) if transform else source_row)
                except (KeyError, ValueError) as error:
                    raise CommandError(
                        f"Valeur invalide dans {filename}, ligne {number} : {error}",
                    ) from error
                lookup = {field: row[field] for field in lookup_fields}
                defaults = {field: value for field, value in row.items() if field not in lookup}
                _, was_created = model.objects.update_or_create(defaults=defaults, **lookup)
                created += int(was_created)
                updated += int(not was_created)

    return created, updated
