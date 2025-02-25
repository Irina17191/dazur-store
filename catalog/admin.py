from django.contrib import admin
from unicodedata import category

from catalog.models import Category, Color, Product


class ProductAdmin(admin.ModelAdmin):        # цей клас відповідає за відображення Product у адмінці (тобто покращюю відображення для зручності)
    list_display = ["name", "category", "price", "available", ]        # цей атрибут відповідає за відображення списку об'єктів в адмінці
    list_filter = ["category", "available", ]        # цей атрибут дозволяє фільтрувати Product по певному полю
    search_fields = ["name", "category__name", ]        # цей атрибут дозволяє здійснювати пошук по певному полю серед Product


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product, ProductAdmin)

