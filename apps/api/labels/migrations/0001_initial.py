from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SES510MI_Lst",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("trdt", models.DateField()),
                ("trtm", models.TimeField()),
                ("usiu", models.CharField(max_length=50)),
                ("conu", models.CharField(max_length=20)),
                ("divu", models.CharField(max_length=20)),
                ("prgnu", models.CharField(db_index=True, max_length=50)),
                ("changed_by", models.CharField(max_length=50)),
                ("trans_program", models.CharField(db_index=True, max_length=50)),
                ("op_code", models.CharField(db_index=True, max_length=10)),
                ("changed_role", models.CharField(blank=True, db_index=True, max_length=50)),
                ("changed_fnc", models.CharField(blank=True, db_index=True, max_length=50)),
                ("changed_user", models.CharField(blank=True, max_length=50)),
                ("type_droit", models.CharField(max_length=50)),
                ("code_option", models.CharField(db_index=True, max_length=50)),
                ("autorisee_avant", models.CharField(max_length=10)),
                ("autorisee_apres", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "ses510mi_lst",
                "constraints": [models.UniqueConstraint(fields=("trdt", "trtm", "usiu", "conu", "divu", "prgnu", "type_droit", "code_option"), name="ses510mi_audit_unique")],
            },
        ),
        migrations.CreateModel(
            name="LibelleFonction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code_fonction", models.CharField(max_length=50)),
                ("libelle", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "libelles_fonctions",
                "constraints": [models.UniqueConstraint(fields=("code_fonction",), name="libelle_fonction_code_unique")],
            },
        ),
        migrations.CreateModel(
            name="LibelleOption",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code_option", models.CharField(max_length=50)),
                ("libelle", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "libelles_options",
                "constraints": [models.UniqueConstraint(fields=("code_option",), name="libelle_option_code_unique")],
            },
        ),
        migrations.CreateModel(
            name="LibelleProgramme",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code_programme", models.CharField(max_length=50)),
                ("libelle", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "libelles_programmes",
                "constraints": [models.UniqueConstraint(fields=("code_programme",), name="libelle_programme_code_unique")],
            },
        ),
        migrations.CreateModel(
            name="LibelleRole",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code_role", models.CharField(max_length=50)),
                ("libelle", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "libelles_roles",
                "constraints": [models.UniqueConstraint(fields=("code_role",), name="libelle_role_code_unique")],
            },
        ),
        migrations.CreateModel(
            name="LibelleOpCode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("op_code", models.CharField(max_length=10)),
                ("libelle", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "libelles_op_codes",
                "constraints": [models.UniqueConstraint(fields=("op_code",), name="libelle_op_code_unique")],
            },
        ),
    ]
