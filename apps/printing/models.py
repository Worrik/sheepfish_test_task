from django.db import models


# used for checks and printers
class CheckType(models.TextChoices):
    KITCHEN = "K", "Kitchen"
    CLIENT = "C", "Client"


class Printer(models.Model):
    name = models.CharField(max_length=100, null=False)
    api_key = models.CharField(max_length=128, unique=True)
    check_type = models.CharField(
        max_length=1,
        choices=CheckType.choices,
        null=False,
    )
    point_id = models.ForeignKey("Point", on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("point_id", "check_type")


class Point(models.Model):
    name = models.CharField(max_length=100, null=False)


class CheckStatus(models.TextChoices):
    NEW = "N", "New"
    RENDERED = "R", "Rendered"
    PRINTED = "P", "Printed"


class Check(models.Model):
    printer_id = models.ForeignKey(
        "Printer", on_delete=models.SET_NULL, null=True
    )
    type = models.CharField(
        max_length=1,
        choices=CheckType.choices,
        null=False,
    )
    order = models.JSONField()
    status = models.CharField(
        max_length=1,
        choices=CheckStatus.choices,
        default=CheckStatus.NEW,
    )
    pdf_file = models.FileField(upload_to="pdf/")
