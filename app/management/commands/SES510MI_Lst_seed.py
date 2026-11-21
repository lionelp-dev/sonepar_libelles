from datetime import datetime

from django.core.management.base import BaseCommand

from app.models import SES510MI_Lst
from app.services.label_catalog import synchronize_label_catalogs
from ._csv import seed_csv


class Command(BaseCommand):
    help = "Synchronise SES510MI_Lst depuis le CSV"

    def handle(self, *args, **options):
        def transform(row):
            return {
                "trdt": datetime.strptime(row["TRDT"], "%Y%m%d").date(),
                "trtm": datetime.strptime(row["TRTM"], "%H%M%S").time(),
                "usiu": row["USIU"], "conu": row["CONU"], "divu": row["DIVU"],
                "prgnu": row["PRGNU"], "changed_by": row["Changed by"],
                "trans_program": row["Trans program"], "op_code": row["Op Code"],
                "changed_role": row["Changed role"], "changed_fnc": row["Changed fnc"],
                "changed_user": row["Changed user"], "type_droit": row["type_droit"],
                "code_option": row["code_option"], "autorisee_avant": row["autorisee_avant"],
                "autorisee_apres": row["autorisee_apres"],
            }

        created, updated = seed_csv(
            filename="SES510MI.csv",
            model=SES510MI_Lst,
            fields=(
                "TRDT", "TRTM", "USIU", "CONU", "DIVU", "PRGNU", "Changed by", "Trans program",
                "Op Code", "Changed role", "Changed fnc", "Changed user", "type_droit", "code_option",
                "autorisee_avant", "autorisee_apres",
            ),
            lookup_fields=("trdt", "trtm", "usiu", "conu", "divu", "prgnu", "type_droit", "code_option"),
            transform=transform,
        )
        synchronize_label_catalogs()
        self.stdout.write(self.style.SUCCESS(f"SES510MI synchronisé ({created} créés, {updated} mis à jour)."))
