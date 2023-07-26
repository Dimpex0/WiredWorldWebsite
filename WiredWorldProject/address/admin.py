from django.contrib import admin

from WiredWorldProject.address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['profile', 'city']
