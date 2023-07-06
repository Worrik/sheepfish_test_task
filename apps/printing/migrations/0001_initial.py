# Generated by Django 4.2.3 on 2023-07-06 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Point",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Printer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("api_key", models.CharField(max_length=128, unique=True)),
                (
                    "check_type",
                    models.CharField(
                        choices=[("K", "Kitchen"), ("C", "Client")], max_length=1
                    ),
                ),
                (
                    "point_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="printing.point",
                    ),
                ),
            ],
            options={
                "unique_together": {("point_id", "check_type")},
            },
        ),
        migrations.CreateModel(
            name="Check",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("K", "Kitchen"), ("C", "Client")], max_length=1
                    ),
                ),
                ("order", models.JSONField()),
                (
                    "status",
                    models.CharField(
                        choices=[("N", "New"), ("R", "Rendered"), ("P", "Printed")],
                        default="N",
                        max_length=1,
                    ),
                ),
                ("pdf_file", models.FileField(upload_to="pdf/")),
                (
                    "printer_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="printing.printer",
                    ),
                ),
            ],
        ),
    ]