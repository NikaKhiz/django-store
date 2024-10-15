from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg
from django.core.paginator import Paginator


def categories(request):
    category_queryset = (
        Category.objects
        .prefetch_related('products', 'subcategory__products')
        .annotate(
            category_products=Count('products', distinct=True),
            subcategory_products=Count('subcategory__products', distinct=True)
            )
    )
    
    context = {'categories': category_queryset}

    return render(request, 'category.html', context)


def category_products(request, category_id):
    # Category instance by given id
    category = get_object_or_404(Category, id=category_id)

    # Products from the current category and its subcategories with total price annotation
    products = (
        Product.objects.filter(category=category) | 
        Product.objects.filter(category__in=category.subcategory.all())
    ).distinct().annotate(total_price=F('quantity') * F('price'))


    paginator = Paginator(products, 2)  
    page = request.GET.get('page')
    page_content = paginator.get_page(page)


    products_highest_price = round(products.aggregate(Max('price'))['price__max'], 2)
    products_lower_price = round(products.aggregate(Min('price'))['price__min'], 2)
    products_average_price = round(products.aggregate(Avg('price'))['price__avg'], 2)
    products_total_price = round(products.aggregate(Sum('total_price'))['total_price__sum'], 2)

    context = {
        'products': page_content,
        'highest_price_product': products_highest_price ,
        'lowest_price_product': products_lower_price,
        'products_avg_price': products_average_price,
        'all_products_total_price': products_total_price,
        'category_id': category_id,
    }
    
    return render(request, 'category_products.html', context)


# Product detailed page
def product_show(request, category_id, slug):
    category = get_object_or_404(Category, id=category_id) 
    product = Product.objects.get(category=category, slug=slug)

    context = {'product' : product, 'category_id': category_id}

    return render(request, 'product.html', context)
