import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0006_create_audit_habilitations")]

    operations = [
        migrations.CreateModel(
            name="Habilitations",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_id", models.CharField(max_length=50)),
                ("nom_complet", models.CharField(max_length=255)),
                ("role_id", models.CharField(max_length=50)),
                ("nom_role", models.CharField(max_length=255)),
                ("code_fonction", models.CharField(max_length=50)),
                ("libelle_fonction", models.CharField(max_length=255)),
                ("societe", models.CharField(max_length=20)),
                ("division", models.CharField(max_length=20)),
                ("statut", models.CharField(max_length=10)),
                ("options_autorisees", models.CharField(max_length=255)),
                ("libelles_options_autorisees", models.CharField(max_length=255)),
                ("niveau_acces", models.PositiveSmallIntegerField()),
                ("libelle_niveau_acces", models.CharField(max_length=255)),
                (
                    "audit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habilitations",
                        to="app.audithabilitations",
                    ),
                ),
            ],
            options={
                "db_table": "habilitations",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("audit", "user_id", "role_id", "code_fonction", "societe", "division"),
                        name="habilitation_audit_unique",
                    ),
                ],
            },
        ),
    ]
