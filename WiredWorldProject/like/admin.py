from django.contrib import admin

from WiredWorldProject.like.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'product']
