from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MNS150MI_LstUsers",
            fields=[
                ("user_id", models.CharField(max_length=50, primary_key=True, serialize=False)),
                ("nom_complet", models.CharField(max_length=255)),
                ("statut", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "mns150mi_lst_users",
            },
        ),
    ]
