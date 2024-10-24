from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg, Prefetch
from django.core.paginator import Paginator

products = []
for _ in range(6):
    products.append(
        {
            'category':'Fruits',
            'title': 'Orange',
            'weight': '1kg',
            'origin': 'Agro Farm',
            'quality': 'organic',
            'min_weight': '250',
            'rate': 4,
            'description':'Lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod te incididunt',
            'price': '$4.99',
            'image':'img/fruite-item-1.jpg'
        }
    )

def index(request):
    root_categories = Category.objects.filter(parent=None)

    categories = Category.objects.prefetch_related(Prefetch(
        'products', queryset=Product.objects.prefetch_related('tag')
    ))

    products = []
    for category in categories:
        products.extend(category.products.all())

    context = {'root_categories': root_categories,'categories': categories, 'products': products}

    return render(request, 'index.html', context)

def category_products(request, slug=None):
    root_categories = Category.objects.filter(parent=None)
    
    if slug:
        categories = Category.objects.filter(slug=slug).prefetch_related(Prefetch(
            'products', queryset=Product.objects.prefetch_related('tag')
        )).all()
    else:
        categories = Category.objects.prefetch_related(Prefetch(
            'products', queryset=Product.objects.prefetch_related('tag')
        ))
    
    products = []
    tags = set()
    for category in categories:
        products.extend(category.products.all())
    paginator = Paginator(products, 3)  
    page = request.GET.get('page', 1) 
    page_content = paginator.get_page(page)

    for product in products:
        tags.update(product.tag.all())

    tags = list(tags)



    breadcrumb = [('Shop', 'store:products', None)]
    if slug:
        breadcrumb.append((categories[0].name,'store:products', categories[0].slug))

    context = {
        'root_categories': root_categories,
        'categories': categories, 
        'products': page_content,
        'tags' : tags,
        'breadcrumb': breadcrumb,
        'slug': slug
        }

    return render(request, 'category_products.html', context)


# Product detailed page
def product_show(request, slug='apple'):
    
    context = {'product' : products[3], }

    return render(request, 'product.html', context)


# contacts page
def contact(request):
    return render(request, 'contacts.html')