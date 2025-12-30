from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from tables.models import Table
from orders.models import Order
from billing.models import Bill
from menu.models import MenuItem
from orders.services import place_order
from accounts.permissions import is_waiter


@login_required
def dashboard_view(request):
    data = []

    for table in Table.objects.all().order_by("table_number"):
        active_orders = Order.objects.filter(
            table=table
        ).exclude(status=Order.Status.SERVED).count()

        bill = Bill.objects.filter(table=table).first()

        data.append({
            "table_number": table.table_number,
            "capacity": table.capacity,
            "status": table.status,
            "active_orders": active_orders,
            "bill_status": bill.status if bill else None,
            "bill_total": bill.total if bill else None,
        })

    return render(request, "dashboard.html", {"tables": data})


@login_required
def place_order_view(request):
    if not is_waiter(request.user):
        return HttpResponseForbidden("Only waiters can place orders")

    tables = Table.objects.filter(
        status__in=[Table.Status.AVAILABLE, Table.Status.OCCUPIED]
    )
    menu_items = MenuItem.objects.filter(is_available=True)

    if request.method == "POST":
        table_id = request.POST.get("table")
        table = Table.objects.get(id=table_id)

        items = []
        for menu in menu_items:
            qty = request.POST.get(f"qty_{menu.id}")
            if qty and int(qty) > 0:
                items.append({
                    "menu": menu,
                    "qty": int(qty)
                })

        if items:
            place_order(table, request.user, items)
            return redirect("/dashboard/")

    return render(
        request,
        "place_order.html",
        {
            "tables": tables,
            "menu_items": menu_items
        }
    )
from django.http import HttpResponseForbidden
from accounts.permissions import is_cashier
from billing.services import generate_bill, mark_bill_paid
from billing.models import Bill


@login_required
def billing_view(request):
    if not is_cashier(request.user):
        return HttpResponseForbidden("Only cashiers can access billing")

    tables = Table.objects.filter(
        status__in=[Table.Status.OCCUPIED, Table.Status.BILL_REQUESTED]
    )

    bills = Bill.objects.select_related("table").all()

    if request.method == "POST":
        table_id = request.POST.get("table")
        table = Table.objects.get(id=table_id)

        try:
            generate_bill(table, request.user)
        except Exception as e:
            return render(
                request,
                "billing.html",
                {
                    "tables": tables,
                    "bills": bills,
                    "error": str(e),
                }
            )

        return redirect("/billing/")

    return render(
        request,
        "billing.html",
        {
            "tables": tables,
            "bills": bills,
        }
    )


@login_required
def pay_bill_view(request, bill_id):
    if not is_cashier(request.user):
        return HttpResponseForbidden("Only cashiers can process payments")

    bill = Bill.objects.get(id=bill_id)

    try:
        mark_bill_paid(bill)
    except Exception as e:
        return redirect("/billing/")

    return redirect("/billing/")
from django.shortcuts import get_object_or_404
from orders.models import Order
from accounts.permissions import is_waiter
from django.http import HttpResponseForbidden


@login_required
def mark_order_served_view(request, order_id):
    if not is_waiter(request.user):
        return HttpResponseForbidden("Only waiters can update order status")

    order = get_object_or_404(Order, id=order_id)

    # Prevent invalid transitions
    if order.status != Order.Status.SERVED:
        order.status = Order.Status.SERVED
        order.save()

    return redirect("/dashboard/")
@login_required
def dashboard_view(request):
    tables_data = []

    for table in Table.objects.all().order_by("table_number"):
        active_orders = Order.objects.filter(
            table=table
        ).exclude(status=Order.Status.SERVED)

        bill = Bill.objects.filter(table=table).first()

        tables_data.append({
            "table": table,
            "orders": active_orders,
            "bill": bill,
        })

    return render(
        request,
        "dashboard.html",
        {
            "tables_data": tables_data,
            "is_waiter": is_waiter(request.user),
        }
    )
