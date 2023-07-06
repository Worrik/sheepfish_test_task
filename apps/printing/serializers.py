from rest_framework import serializers

from apps.printing.models import Check, Point, Printer


class PrintSerializer(serializers.Serializer):
    order = serializers.JSONField()
    point_id = serializers.IntegerField()

    def validate_order(self, order: dict) -> dict:
        """
        Check that order does not exists
        """
        order_id = order.get("id")

        if not order_id:
            raise serializers.ValidationError("Must have an id")

        if Check.objects.filter(order__id=order_id).exists():
            raise serializers.ValidationError(
                f"Checks for order #{order_id} already exists"
            )

        return order

    def validate_point_id(self, point_id: int) -> int:
        """
        Check that point has printers
        """
        if not Printer.objects.filter(point_id=point_id).exists():
            raise serializers.ValidationError("Printers not found")
        return point_id


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ["id", "printer_id", "type", "order", "status", "pdf_file"]
