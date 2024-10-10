from django.http import HttpResponse, JsonResponse
from .models import Category

# Display provided products
def product_index(request):
    return HttpResponse('products list view')


# Display a specific product detail 
def product_show(request,id):
    return HttpResponse(f'details for product - {id}', )

# Fetch all categories with its parents
def categories(request):
    
    categories = Category.objects.select_related('parent_category').all()
    context = {
        'categories': [
            {
                'id': category.id,
                'name': category.name,
                'parent': category.parent_category.name if category.parent_category else None
            } for category in categories
        ]
    }

    return JsonResponse(context)


def products(request):
    return HttpResponse('products with categories')
