from django.contrib import admin
from .models import Branches, Department, Employee, ServiceType, PaymentMethod, ITService, Equipment, Stock, Provider, Client, Order, Post, Contract

# Register your models here.
admin.site.register(Branches)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(ServiceType)
admin.site.register(ITService)
admin.site.register(Equipment)
admin.site.register(Stock)
admin.site.register(Provider)
admin.site.register(Client)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('Client', 'OrderDate', 'OrderRequirement', 'OrderStatus','Employee', 'PaymentMethod')
    list_filter = ['OrderStatus']
    search_fields = ['Client']


admin.site.register(Order, OrderAdmin)
admin.site.register(Post)
admin.site.register(PaymentMethod)
admin.site.register(Contract)

