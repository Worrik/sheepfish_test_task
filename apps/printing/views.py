from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, views, mixins, status
from apps.printing.models import Check, CheckStatus, Printer

from apps.printing.serializers import CheckSerializer, PrintSerializer
from apps.printing.tasks import print_check


class PrintView(views.APIView):
    serializer_class = PrintSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)

        order = serializer.data["order"]
        point_id = serializer.data["point_id"]

        printers = Printer.objects.filter(point_id=point_id)

        for printer in printers:
            check = Check.objects.create(
                printer_id=printer,  # type: ignore
                type=printer.check_type,
                order=order,
            )
            print_check.delay(check.id)  # type: ignore

        return Response({"ok": True})


class CheckViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Check.objects.filter()
    serializer_class = CheckSerializer
    permission_classes = []

    def get_queryset(self) -> QuerySet[Check]:
        qs = super().get_queryset()
        printer_id = self.request.GET.get("printer_id")
        if printer_id:
            qs = qs.filter(printer_id=printer_id)
        return qs

    @action(detail=True, methods=["put"])
    def set_printed(self, request: Request, pk=None) -> Response:
        check = self.get_object()
        check.status = CheckStatus.PRINTED
        check.save()
        return Response(
            status=status.HTTP_302_FOUND,
            headers={"Location": check.pdf_file.url},
        )
