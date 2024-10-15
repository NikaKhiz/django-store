from django.http import JsonResponse
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum


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



def category_products(request, id):
    # Category instance by given id
    category = get_object_or_404(Category, id=id)
    # products products from the current category and its subcategories
    products = Product.objects.filter(category=category) | Product.objects.filter(category__in=category.subcategory.all())
    # total price for the products
    product_subtotal = products.annotate(total_price=F('quantity') * F('price')).aggregate(sub_total=Sum('total_price'))

    context = {
        'products': products,
        'product_subtotal': round(product_subtotal['sub_total'], 2)  
    }
    
    return render(request, 'category_products.html', context)


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
