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
    list_display = ('name', 'price', 'quantity', 'total_prices', 'is_published', 'created_at', 'updated_at')
    search_fields = ('name', 'slug',)
    list_filter = ('is_published', 'category')
    autocomplete_fields = ('category', )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    date_hierarchy = 'updated_at'

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', ('price', 'quantity'), 'is_published')
        }),
        ('Advanced options', {
            'classes': ('collapse', ),
            'fields': ('image', )
        }),
    )

    @admin.display
    def total_prices(self, obj):
        return obj.price * obj.quantity