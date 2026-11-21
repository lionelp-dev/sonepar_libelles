from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Synchronise l'audit SES510 et les référentiels depuis les CSV."""

    help = "Synchronise l'audit SES510 et ses référentiels depuis les CSV"

    def handle(self, *args, **options):
        for commande in (
            "SES510MI_Lst_seed",
            "libelles_fonctions_seed",
            "libelles_programmes_seed",
            "libelles_roles_seed",
            "libelles_options_seed",
            "libelles_op_codes_seed",
        ):
            call_command(commande)

        self.stdout.write(self.style.SUCCESS("L'audit SES510 et ses référentiels ont été synchronisés."))
