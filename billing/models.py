from django.db import models
from django.contrib.auth.models import User
from tables.models import Table

class Bill(models.Model):

    class Status(models.TextChoices):
        NOT_GENERATED = "NOT_GENERATED", "Not Generated"
        PENDING_PAYMENT = "PENDING_PAYMENT", "Pending Payment"
        PAID = "PAID", "Paid"

    table = models.OneToOneField(Table, on_delete=models.PROTECT)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING_PAYMENT
    )
    generated_by = models.ForeignKey(User, on_delete=models.PROTECT)
    generated_at = models.DateTimeField(auto_now_add=True)
