# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Merceria, Etiqueta,Bolsa


@admin.register(Merceria)
class MerceriaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'codigo', 'cantidad']
    list_display = ['nombre', 'codigo', 'cantidad']

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    fields = ['tipo', 'talla', 'cantidad']
    list_display = ['tipo', 'talla', 'cantidad']

@admin.register(Bolsa)
class BolsaAdmin(admin.ModelAdmin):
    fields = ['cantidad', 'modelo']
    list_display = ['cantidad', 'modelo']

