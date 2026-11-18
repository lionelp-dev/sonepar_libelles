from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0007_create_habilitations")]

    operations = [
        migrations.CreateModel(
            name="MNS410MI_LstRolesByUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_id", models.CharField(max_length=50)),
                ("role_id", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "mns410mi_lst_roles_by_user",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user_id", "role_id"),
                        name="mns410mi_user_role_unique",
                    ),
                ],
            },
        ),
    ]
