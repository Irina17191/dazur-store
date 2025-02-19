from django.contrib import admin

from catalog.models import Category, Color, Product


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)

