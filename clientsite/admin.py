from django.contrib import admin
from .models import Order, OrderItem, RequestForQuotation, RequestForService
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(RequestForQuotation)
admin.site.register(RequestForService)