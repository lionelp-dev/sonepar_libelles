from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0008_create_mns410mi_lst_roles_by_user")]

    operations = [
        migrations.CreateModel(
            name="SES400MI_LstAuthByRole",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role_id", models.CharField(max_length=50)),
                ("code_fonction", models.CharField(max_length=50)),
                ("libelle_fonction", models.CharField(max_length=255)),
                ("societe", models.CharField(max_length=20)),
                ("division", models.CharField(max_length=20)),
                ("statut", models.CharField(max_length=10)),
                ("code_option", models.CharField(blank=True, max_length=10)),
            ],
            options={
                "db_table": "ses400mi_lst_auth_by_role",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("role_id", "code_fonction", "societe", "division", "code_option"),
                        name="ses400mi_role_fonction_option_unique",
                    ),
                ],
            },
        ),
    ]
