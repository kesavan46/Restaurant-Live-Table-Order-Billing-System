from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.drf_permissions import IsWaiter
from tables.models import Table
from menu.models import MenuItem
from .services import place_order

class PlaceOrderAPI(APIView):
    permission_classes = [IsWaiter]

    def post(self, request):
        table_id = request.data.get("table_id")
        items_data = request.data.get("items", [])

        if not items_data:
            return Response({"error": "No items provided"}, status=400)

        table = Table.objects.get(id=table_id)

        items = []
        for item in items_data:
            menu = MenuItem.objects.get(id=item["menu_id"], is_available=True)
            items.append({"menu": menu, "qty": item["quantity"]})

        order = place_order(table, request.user, items)

        return Response(
            {"message": "Order placed", "order_id": order.id},
            status=status.HTTP_201_CREATED
        )
