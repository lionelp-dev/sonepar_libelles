from django.core.management.base import BaseCommand

from app.services.audit_habilitations import generate_audit


class Command(BaseCommand):
    """Affiche l'audit des habilitations M3."""

    help = "Génère un audit des habilitations M3"

    def handle(self, *args, **options):
        audit, nombre_habilitations = generate_audit()

        self.stdout.write(
            self.style.SUCCESS(
                f"Audit #{audit.pk} : {nombre_habilitations} habilitation(s) générée(s)."
            )
        )
