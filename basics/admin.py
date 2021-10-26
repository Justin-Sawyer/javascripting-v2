from django.contrib import admin

from .models import Article, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'summary',
        'date_added',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)