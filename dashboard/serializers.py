from rest_framework import serializers

class TableDashboardSerializer(serializers.Serializer):
    table_id = serializers.IntegerField()
    table_number = serializers.IntegerField()
    capacity = serializers.IntegerField()
    status = serializers.CharField()
    active_orders = serializers.IntegerField()
    bill_status = serializers.CharField(allow_null=True)
    bill_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, allow_null=True
    )
