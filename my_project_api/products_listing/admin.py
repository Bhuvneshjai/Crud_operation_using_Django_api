from django.contrib import admin
from products_listing.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','product_present',)
    search_fields = ('product_name',)

admin.site.register(Product, ProductAdmin)