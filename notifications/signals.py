from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order

@receiver(post_save, sender=Order)
def notify_kitchen_on_order(sender, instance, created, **kwargs):
    if created and instance.status == Order.Status.PLACED:
        # Simulate kitchen notification
        print(
            f"[KITCHEN NOTIFY] New order #{instance.id} "
            f"for Table {instance.table.table_number}"
        )
