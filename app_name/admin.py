from django.contrib import admin
from app_name.models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductCharacteristicInline]

admin.site.register(Product, ProductAdmin)


