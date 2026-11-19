from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0009_create_ses400mi_lst_auth_by_role")]

    operations = [
        migrations.CreateModel(
            name="MNS110MI_Lst",
            fields=[
                ("code_fonction", models.CharField(max_length=50, primary_key=True, serialize=False)),
                ("programme_m3", models.CharField(max_length=50)),
                ("categorie_fonction", models.CharField(max_length=20)),
                ("autorisation_requise", models.CharField(max_length=1)),
            ],
            options={"db_table": "mns110mi_lst"},
        ),
        migrations.CreateModel(
            name="SES401_CMNPUS",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_id", models.CharField(max_length=50)),
                ("nom_complet", models.CharField(max_length=255)),
                ("programme_m3", models.CharField(max_length=50)),
                ("societe", models.CharField(max_length=20)),
                ("division", models.CharField(max_length=20)),
                ("role_id", models.CharField(max_length=50)),
                ("code_option", models.CharField(blank=True, max_length=10)),
            ],
            options={
                "db_table": "ses401_cmpnus",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user_id", "programme_m3", "societe", "division", "role_id", "code_option"),
                        name="ses401_user_programme_role_option_unique",
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="SES510MI_Lst",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("id_evenement", models.CharField(max_length=50)),
                ("trdt", models.DateField()),
                ("trtm", models.TimeField()),
                ("usiu", models.CharField(max_length=50)),
                ("conu", models.CharField(max_length=20)),
                ("divu", models.CharField(max_length=20)),
                ("prgnu", models.CharField(max_length=50)),
                ("modifie_par", models.CharField(max_length=50)),
                ("programme_origine", models.CharField(max_length=50)),
                ("code_operation", models.CharField(max_length=10)),
                ("role_modifie", models.CharField(blank=True, max_length=50)),
                ("fonction_modifiee", models.CharField(blank=True, max_length=50)),
                ("utilisateur_modifie", models.CharField(blank=True, max_length=50)),
                ("code_option", models.CharField(blank=True, max_length=10)),
                ("autorisee_avant", models.CharField(max_length=10)),
                ("autorisee_apres", models.CharField(max_length=10)),
                ("options_de_base_modifiees", models.CharField(blank=True, max_length=10)),
                ("options_associees_modifiees", models.CharField(blank=True, max_length=10)),
                ("touches_fonction_modifiees", models.CharField(blank=True, max_length=10)),
            ],
            options={
                "db_table": "ses510mi_lst",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("id_evenement", "code_option"),
                        name="ses510_evenement_option_unique",
                    ),
                ],
            },
        ),
    ]
