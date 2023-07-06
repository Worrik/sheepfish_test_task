from django.contrib import admin
from .models import CheckType, Printer, Point, CheckStatus, Check


class PrinterAdmin(admin.ModelAdmin):
    list_display = ("name", "api_key", "check_type", "point_id")
    list_filter = ("check_type", "point_id")
    search_fields = ("name", "api_key")


class PointAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CheckAdmin(admin.ModelAdmin):
    list_display = ("printer_id", "type", "status", "pdf_file")
    list_filter = ("printer_id", "type", "status")
    search_fields = ("printer_id__name", "pdf_file")


admin.site.register(Printer, PrinterAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Check, CheckAdmin)
