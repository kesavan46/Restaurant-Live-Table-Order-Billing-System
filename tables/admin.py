from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "capacity", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("table_number",)
