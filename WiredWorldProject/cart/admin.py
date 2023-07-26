from django.contrib import admin

from WiredWorldProject.cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['profile', 'product', 'quantity']
