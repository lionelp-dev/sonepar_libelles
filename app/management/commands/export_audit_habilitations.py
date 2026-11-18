from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from app.models import AuditHabilitations
from app.services.audit_habilitations import write_audit_csv


class Command(BaseCommand):
    """Exporte le dernier audit des habilitations en CSV."""

    help = "Exporte le dernier audit des habilitations en CSV"

    def handle(self, *args, **options):
        audit = AuditHabilitations.objects.order_by("-created_at", "-pk").first()
        if audit is None:
            raise CommandError("Aucun audit des habilitations n'existe.")

        dossier_exports = Path(settings.BASE_DIR) / "exports"
        dossier_exports.mkdir(exist_ok=True)
        date_audit = audit.created_at.strftime("%Y%m%d_%H%M%S")
        fichier_csv = dossier_exports / f"audit_habilitations_{audit.pk}_{date_audit}.csv"

        with fichier_csv.open("w", encoding="utf-8-sig", newline="") as fichier:
            write_audit_csv(audit, fichier)

        self.stdout.write(self.style.SUCCESS(f"Fichier généré : {fichier_csv}"))
