from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Synchronise toutes les données M3 et les référentiels depuis les CSV."""

    help = "Synchronise toutes les données M3 depuis les CSV"

    def handle(self, *args, **options):
        for commande in (
            "libelles_fonctions_seed",
            "libelles_options_seed",
            "MNS110MI_Lst_seed",
            "MNS150MI_LstUsers_seed",
            "MNS405MI_Lst_seed",
            "MNS410MI_LstRolesByUser_seed",
            "SES400MI_LstAuthByRole_seed",
            "SES401_CMNPUS_seed",
            "SES510MI_Lst_seed",
        ):
            call_command(commande)

        self.stdout.write(self.style.SUCCESS("Toutes les sources CSV ont été synchronisées."))
