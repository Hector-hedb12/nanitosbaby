# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Merceria, Etiqueta, Bolsa, Tela


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

@admin.register(Tela)
class TelaAdmin(admin.ModelAdmin):
    fields = ['tipo', 'peso']
    list_display = ['tipo', 'peso']

