from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0001_create_mns150mi_lst_users")]

    operations = [
        migrations.CreateModel(
            name="LibellesFonctions",
            fields=[
                ("code_fonction", models.CharField(max_length=50, primary_key=True, serialize=False)),
                ("libelle_fonction", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={"db_table": "libelles_fonctions"},
        ),
    ]
