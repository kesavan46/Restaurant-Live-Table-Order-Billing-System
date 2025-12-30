from tables.models import Table
from orders.models import Order, OrderItem
from django.db import transaction
from django.core.exceptions import ValidationError

@transaction.atomic
def place_order(table, user, items):

    if table.status == Table.Status.CLOSED:
        raise ValidationError("Cannot place order on closed table")

    if table.status == Table.Status.BILL_REQUESTED:
        raise ValidationError("Bill already requested for this table")

    if table.status == Table.Status.AVAILABLE:
        table.status = Table.Status.OCCUPIED
        table.save()

    order = Order.objects.create(
        table=table,
        created_by=user
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            menu_item=item["menu"],
            quantity=item["qty"],
            price_snapshot=item["menu"].price
        )

    return order
