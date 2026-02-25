from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # """
    # Customize how Item appears in admin panel.
    # """

    list_display = ('title', 'price', 'owner', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)