from celery import shared_task
from django.template.loader import render_to_string
from django.core.files.base import ContentFile

import requests
import base64
import json

from apps.printing.models import Check, CheckStatus
from test_task.settings import WKHTMLTOPDF_URL


session = requests.Session()


@shared_task
def print_check(check_id: int) -> None:
    check = Check.objects.get(pk=check_id)
    order_id = check.order["id"]

    html_content = render_to_string(
        "wkhtmltopdf/check.html", check.order
    ).encode("utf-8")
    data = {"contents": base64.b64encode(html_content).decode("utf-8")}
    headers = {"Content-Type": "application/json"}

    response = session.post(
        WKHTMLTOPDF_URL,
        data=json.dumps(data),
        headers=headers,
    )

    file_name = f"{order_id}_{check.type}.pdf"
    file = ContentFile(response.content, name=file_name)

    check.pdf_file.save(file_name, file)
    check.status = CheckStatus.RENDERED
    check.save()
