from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg


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

    # Products from the current category and its subcategories with total price annotation
    products = (
        Product.objects.filter(category=category) | 
        Product.objects.filter(category__in=category.subcategory.all())
    ).distinct().annotate(total_price=F('quantity') * F('price'))


    products_highest_price = round(products.aggregate(Max('total_price'))['total_price__max'], 2)
    products_lower_price = round(products.aggregate(Min('total_price'))['total_price__min'], 2)
    products_average_price = round(products.aggregate(Avg('total_price'))['total_price__avg'], 2)
    products_total_price = round(products.aggregate(Sum('total_price'))['total_price__sum'], 2)

    context = {
        'products': products,
        'highest_price_product': products_highest_price ,
        'lowest_price_product': products_lower_price,
        'products_avg_price': products_average_price,
        'all_products_total_price': products_total_price,
    }
    
    return render(request, 'category_products.html', context)


# Product detailed page
def product_show(request,id):
    product = get_object_or_404(Product, id=id)

    context = {'product' : product}

    return render(request, 'product.html', context)
