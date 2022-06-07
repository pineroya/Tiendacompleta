from django.contrib import admin
from .models import CategoriaModel, PostModel

# Register your models here.

class CategoriaModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaModel, CategoriaModelAdmin)
admin.site.register(PostModel, PostModelAdmin)