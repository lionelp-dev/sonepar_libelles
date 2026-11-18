from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0002_create_libelles_fonctions")]

    operations = [
        migrations.CreateModel(
            name="LibellesNiveauxAcces",
            fields=[
                ("niveau_acces", models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ("libelle_niveau_acces", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={"db_table": "libelles_niveaux_acces"},
        ),
    ]
