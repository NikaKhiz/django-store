from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parent',)
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'parent')
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'is_published', 'created_at', 'updated_at')
    search_fields = ('name', 'slug',)
    list_filter = ('is_published', 'category')
    filter_horizontal = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)  

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', ('price', 'quantity',), 'is_published', 'description' )
        }),
        ('Advanced options', {
            'classes': ('collapse', ),
            'fields': ('category', 'image')
        }),
    )
