from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "table",
        "subtotal",
        "tax",
        "total",
        "status",
        "generated_by",
        "generated_at",
    )
    list_filter = ("status",)
    readonly_fields = ("subtotal", "tax", "total", "generated_at")
