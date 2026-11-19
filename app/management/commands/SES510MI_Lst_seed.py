from datetime import datetime

from django.core.management.base import BaseCommand

from app.models import SES510MI_Lst
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise SES510MI_Lst depuis le CSV"

    def handle(self, *args, **options):
        def transform(row):
            return {
                **{key.lower(): value for key, value in row.items()},
                "trdt": datetime.strptime(row["TRDT"], "%Y%m%d").date(),
                "trtm": datetime.strptime(row["TRTM"], "%H%M%S").time(),
            }

        created, updated = seed_csv(
            filename="SES510MI_Lst.csv",
            model=SES510MI_Lst,
            fields=(
                "id_evenement", "TRDT", "TRTM", "USIU", "CONU", "DIVU", "PRGNU", "modifie_par", "programme_origine",
                "code_operation", "role_modifie", "fonction_modifiee", "utilisateur_modifie", "code_option",
                "autorisee_avant", "autorisee_apres", "options_de_base_modifiees", "options_associees_modifiees",
                "touches_fonction_modifiees",
            ),
            lookup_fields=("id_evenement", "code_option"),
            transform=transform,
        )
        self.stdout.write(self.style.SUCCESS(f"Journal des modifications synchronisé ({created} créées, {updated} mises à jour)."))
