from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0002_create_libelles_fonctions")]

    operations = [
        migrations.CreateModel(
            name="LibellesOptions",
            fields=[
                ("code_option", models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ("libelle_option", models.CharField(max_length=255)),
                ("libelle_anglais", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={"db_table": "libelles_options"},
        ),
    ]
