# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Category, Size, ProductAmount, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    list_display_links = None
    list_editable = ['name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    list_display_links = None
    list_editable = ['name']


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    fields = ['product', 'size', 'amount']
    list_display = ['product', 'size', 'amount']
    list_editable = ['amount']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image', 'category']
    list_display = ['name', 'description', 'price', 'category']
