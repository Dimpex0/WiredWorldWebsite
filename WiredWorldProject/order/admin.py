from django.contrib import admin

from WiredWorldProject.order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['profile', 'product', 'quantity', 'date']
    search_fields = ['profile__email']
