from django.contrib import admin

# Register your models here.

from .models import Category, Product, OrderDetail, OrderItems,ShippingInfo

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price","discount",)
    list_filter = ("name", "price", "discount", "date_created", "date_modified",)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "total_amout",  "shippingInfo",)
    list_filter = ("shippingInfo", "product", "quantity",)
    
    
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ("orderDetails", "customer", "state","city",)
    list_filter = ("orderDetails", "customer", "state", "city")
    

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("completed", "customer", "status", "date" , "transanction_id")
    list_filter = ("completed", "customer", "status", "date")
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
admin.site.register(ShippingInfo, ShippingInfoAdmin)