from django.contrib import admin

from order.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['total_product', 'total_price', 'created_date']
    list_filter = ['created_date']
    search_fields = ['description']
