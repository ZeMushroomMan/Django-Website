from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'price', 'in_stock', 'id',]
    list_filter = ['in_stock','is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}