from django.contrib import admin
from .models import Stock, Product

# class StockInline(admin.TabularInline):
#     model = Stock
#     extra = 2
#
# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 2

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address', 'positions']
    # inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    # inlines = [StockInline]
