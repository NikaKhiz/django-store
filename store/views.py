from django.http import JsonResponse
from .models import Category, Product
from django.shortcuts import render
from django.db.models import Count


def categories(request):
    category_queryset = (
        Category.objects
        .prefetch_related('products', 'subcategory__products')
        .annotate(
            category_products=Count('products'),
            subcategory_products=Count('subcategory__products')
            )
    )
    
    context = {'categories': category_queryset}

    return render(request, 'category.html', context)


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


# Display a specific product details 
def product_show(request,id):
    try:
        product = Product.objects.get(id=id)
        context = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image': f'http://localhost:8000{product.image.url}' if product.image else None,
            'categories': [category.name for category in product.category.all()]
        }
        return JsonResponse(context)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
