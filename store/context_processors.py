from .models import Category

def root_categories_context(request):
    root_categories = Category.objects.filter(parent__isnull=True)

    return {
        'root_categories': root_categories,
    }