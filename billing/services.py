from billing.models import Bill
from orders.models import OrderItem, Order
from tables.models import Table
from django.core.exceptions import ValidationError
from decimal import Decimal

TAX_PERCENT = Decimal("0.05")

def generate_bill(table, user):

    if Bill.objects.filter(table=table).exists():
        raise ValidationError("Bill already generated for this table")

    served_orders = Order.objects.filter(
        table=table,
        status=Order.Status.SERVED
    )

    if not served_orders.exists():
        raise ValidationError("No served orders for this table")

    items = OrderItem.objects.filter(order__in=served_orders)

    subtotal = sum(item.price_snapshot * item.quantity for item in items)
    tax = subtotal * TAX_PERCENT
    total = subtotal + tax

    bill = Bill.objects.create(
        table=table,
        subtotal=subtotal,
        tax=tax,
        total=total,
        generated_by=user,
        status=Bill.Status.PENDING_PAYMENT
    )

    table.status = Table.Status.BILL_REQUESTED
    table.save()

    return bill

def mark_bill_paid(bill):

    if bill.status == Bill.Status.PAID:
        raise ValidationError("Bill already paid")

    bill.status = Bill.Status.PAID
    bill.save()

    table = bill.table
    table.status = Table.Status.AVAILABLE
    table.save()
