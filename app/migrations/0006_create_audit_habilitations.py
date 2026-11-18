from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("app", "0005_create_mns405mi_lst")]

    operations = [
        migrations.CreateModel(
            name="AuditHabilitations",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "audit_habilitations"},
        ),
    ]
