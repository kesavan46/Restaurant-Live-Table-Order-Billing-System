from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

from accounts.drf_permissions import IsCashier
from tables.models import Table
from orders.models import Order   # ✅ CORRECT
from .models import Bill
from .services import generate_bill, mark_bill_paid
from accounts.drf_permissions import IsWaiter

class GenerateBillAPI(APIView):
    permission_classes = [IsCashier]

    def post(self, request):
        try:
            table_id = request.data.get("table_id")
            table = Table.objects.get(id=table_id)

            bill = generate_bill(table, request.user)

            return Response(
                {"message": "Bill generated", "bill_id": bill.id},
                status=201
            )

        except ValidationError as e:
            return Response({"error": str(e)}, status=400)

class PayBillAPI(APIView):
    permission_classes = [IsCashier]

    def post(self, request, bill_id):
        bill = Bill.objects.get(id=bill_id)

        if bill.status == Bill.Status.PAID:
            return Response({"error": "Bill already paid"}, status=400)

        mark_bill_paid(bill)

        return Response({"message": "Payment successful"})

class UpdateOrderStatusAPI(APIView):
    permission_classes = [IsWaiter]

    def patch(self, request, order_id):
        order = Order.objects.get(id=order_id)
        new_status = request.data.get("status")

        if new_status not in Order.Status.values:
            return Response({"error": "Invalid status"}, status=400)

        order.status = new_status
        order.save()

        return Response({"message": "Order updated"})
