from django.contrib import admin

from product.models import ProductModel, ColorModel, SizeModel, CategoryModel, ProductImageModel, StoreModel


class ProductImageStackedInLine(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title', 'last_name']
    inlines = [ProductImageStackedInLine]


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title', 'last_name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title', 'last_name']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title', 'last_name']


@admin.register(StoreModel)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    list_filter = ['created_date']
    search_fields = ['name', 'description']
