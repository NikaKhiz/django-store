from .models import Category
from django.core.cache import cache

def root_categories_context(request):
    root_categories = cache.get('root_categories_cache')
    
    if root_categories is None:
        root_categories = Category.objects.filter(parent__isnull=True)
        cache.set('root_categories_cache', root_categories, 60 * 1)

    return {
        'root_categories': root_categories,
    }