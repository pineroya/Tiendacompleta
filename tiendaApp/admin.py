from django.contrib import admin
from .models import CategoriaProductoModel, ProductoModel

# Register your models here.

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProductoModel, CategoriaProductoAdmin)
admin.site.register(ProductoModel, ProductoAdmin)