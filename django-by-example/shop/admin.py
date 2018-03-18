from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin

# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}
    # prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    # prepopulated_fields = {'slug':('name',)}

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}

admin.site.register(Product, ProductAdmin)


