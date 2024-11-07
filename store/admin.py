from django.contrib import admin
from .models import Category, Product, ProductTag
from admin_auto_filters.filters import AutocompleteFilter
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin


class CategoryFilter(AutocompleteFilter):
    title = 'Category' 
    field_name = 'parent' 

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = [CategoryFilter]
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_select_related = ('parent',)
    list_editable = ('parent',)
    list_per_page = 10
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'parent', 'image', 'description')
        }),
    )



class ProductFilterByCategory(AutocompleteFilter):
    title = 'Category' 
    field_name = 'category' 
class ProductFilterByTag(AutocompleteFilter):
    title = 'Tag' 
    field_name = 'tag' 

@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'price', 'quantity', 'total_prices', 'quality', 'origin', 'weight', 'healthy', 'is_published', 'created_at', 'updated_at')
    search_fields = ('name', 'slug',)
    list_filter = [ProductFilterByCategory, ProductFilterByTag, 'is_published', 'healthy']
    autocomplete_fields = ('category', 'tag')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at', 'price', 'quantity', 'name')
    date_hierarchy = 'updated_at'
    list_per_page = 10
    list_editable = ('price', 'quantity', 'origin', 'quality', 'weight', 'is_published', 'healthy' )


    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'tag', ('price', 'quantity'), ('is_published', 'healthy'), 'origin', 'weight', 'quality')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('image', 'description')
        }),
    )

    @admin.display(description=_('total price'))
    def total_prices(self, obj):
        return obj.price * obj.quantity
    


@admin.register(ProductTag)
class ProductTagAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'updated_at', 'created_at')
    search_fields = ('name',)
    ordering = ('name', )
    date_hierarchy = 'updated_at'
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
    )