from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'order_status', 'quantity', 'created_at', 'updated_at']
    list_filter = ['created_at', 'order_status', 'quantity']
admin.site.register(Order, OrderAdmin)