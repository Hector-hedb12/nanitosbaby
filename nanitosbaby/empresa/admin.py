from django.contrib import admin

from .models import Descripcion


@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    fields = ['titulo', 'contenido', 'orden']
    list_display = ['titulo', 'orden']
