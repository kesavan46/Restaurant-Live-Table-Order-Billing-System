from django.db import models

class Table(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        OCCUPIED = "OCCUPIED", "Occupied"
        BILL_REQUESTED = "BILL_REQUESTED", "Bill Requested"
        CLOSED = "CLOSED", "Closed"

    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.status})"
