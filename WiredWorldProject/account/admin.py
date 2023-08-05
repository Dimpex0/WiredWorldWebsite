from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from WiredWorldProject.account.models import Client, Profile

UserModel = get_user_model()


@admin.register(UserModel)
class ClientAdmin(UserAdmin):
    list_display = ['email', 'is_staff', 'is_superuser']
    readonly_fields = ['date_joined']
    ordering = ['email']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'password1', 'password2'),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'first_name']
    search_fields = ['email', 'first_name', 'last_name']
