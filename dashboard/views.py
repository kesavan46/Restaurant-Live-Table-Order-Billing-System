from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.drf_permissions import IsManager
from tables.models import Table
from orders.models import Order
from billing.models import Bill
from .serializers import TableDashboardSerializer


class TableDashboardAPI(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        data = []

        tables = Table.objects.all().order_by("table_number")

        for table in tables:
            active_orders = Order.objects.filter(
                table=table
            ).exclude(status=Order.Status.SERVED).count()

            bill = Bill.objects.filter(table=table).first()

            data.append({
                "table_id": table.id,
                "table_number": table.table_number,
                "capacity": table.capacity,
                "status": table.status,
                "active_orders": active_orders,
                "bill_status": bill.status if bill else None,
                "bill_total": bill.total if bill else None,
            })

        serializer = TableDashboardSerializer(data, many=True)
        return Response(serializer.data)
