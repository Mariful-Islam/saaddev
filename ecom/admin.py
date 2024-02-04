from django.contrib import admin
from ecom.models import DeliveryPlace, Product, Cart, OrderItem
# Register your models here.


admin.site.register(DeliveryPlace)

class ProductModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'price')

admin.site.register(Product,  ProductModel)

class CartModel(admin.ModelAdmin):
    list_display = ('username', 'product')

admin.site.register(Cart, CartModel)

class OrderItemModel(admin.ModelAdmin):
    list_display = ('username', 'product_name', 'product_quantity')

admin.site.register(OrderItem, OrderItemModel)
