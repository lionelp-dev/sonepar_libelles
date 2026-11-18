from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0004_create_libelles_options")]

    operations = [
        migrations.CreateModel(
            name="MNS405MI_Lst",
            fields=[
                ("role_id", models.CharField(max_length=50, primary_key=True, serialize=False)),
                ("nom_role", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
            ],
            options={"db_table": "mns405mi_lst"},
        ),
    ]
