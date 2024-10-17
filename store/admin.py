from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parent',)
    ordering = ('name',)
    list_select_related = ('parent',)
    
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
    ordering = ('-created_at', 'price', 'quantity', 'name')
    date_hierarchy = 'updated_at'
    list_per_page = 10
    list_editable = ('price', 'quantity', 'is_published')


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