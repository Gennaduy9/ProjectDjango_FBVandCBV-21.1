# admin1
# пароль 12345


from django.contrib import admin

from carsaudi.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'category', 'photo', 'price', 'color',)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category',)
    search_fields = ('name', 'description',)