from django.http import HttpResponse, JsonResponse
from .models import Category, Product

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


# Fetch all products with its cateogies and display results
def products(request):
    products = Product.objects.prefetch_related('category').all()
    context = {
        'products': [
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image': f'http://localhost:8000{product.image.url}' if product.image else None,
                'categories': [category.name for category in product.category.all()]
            } for product in products
        ]
    }

    return JsonResponse(context)
