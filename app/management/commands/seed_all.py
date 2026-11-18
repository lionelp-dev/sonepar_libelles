from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Lance tous les seeders, sauf celui des habilitations."""

    help = "Lance tous les seeders, sauf celui des habilitations"

    def handle(self, *args, **options):
        for commande in (
            "libelles_fonctions_seed",
            "libelles_niveaux_acces_seed",
            "libelles_options_seed",
            "MNS150MI_LstUsers_seed",
            "MNS405MI_Lst_seed",
            "MNS410MI_LstRolesByUser_seed",
            "SES400MI_LstAuthByRole_seed",
        ):
            call_command(commande)

        self.stdout.write(self.style.SUCCESS("Tous les seeders ont été lancés."))
