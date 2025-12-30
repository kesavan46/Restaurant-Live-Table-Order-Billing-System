from django.db import models
from django.contrib.auth.models import User
from tables.models import Table
from menu.models import MenuItem

class Order(models.Model):

    class Status(models.TextChoices):
        PLACED = "PLACED", "Placed"
        IN_KITCHEN = "IN_KITCHEN", "In Kitchen"
        SERVED = "SERVED", "Served"

    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLACED
    )
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_snapshot = models.DecimalField(max_digits=8, decimal_places=2)
