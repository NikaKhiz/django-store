from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg, Prefetch
from django.core.paginator import Paginator
from store.forms import ProductForm


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

    products = Product.objects.filter(category__in=categories)

    context = {'root_categories': root_categories,'categories': categories, 'products': products}

    return render(request, 'index.html', context)

def category_products(request, slug=None):
    # for displaying root categories in navigation
    root_categories = Category.objects.filter(parent=None)
    
    # for handling template rendering accordinly if slug exists
    if slug:
        categories = Category.objects.filter(slug=slug).prefetch_related(Prefetch(
            'products', queryset=Product.objects.prefetch_related('tag')
        )).all()
    else:
        categories = Category.objects.prefetch_related(Prefetch(
            'products', queryset=Product.objects.prefetch_related('tag')
        ))
    
    products = Product.objects.filter(category__in=categories)
    
    # handle post request
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = request.POST.get('product_name')
            product_price = request.POST.get('product_price')
            tag = request.POST.get('product_tag')
            sort_option = request.POST.get('sort_list')
            if product_name:
                products = products.filter(name__icontains=product_name)
            if product_price:
                products = products.filter(price__lte=product_price)
            if tag:
                products = products.filter(tag__name__icontains=tag)

            if sort_option == 'price_up':
                products = products.order_by('price')
            elif sort_option == 'price_down':
                products = products.order_by('-price')
            elif sort_option == 'created_at':
                products = products.order_by('-created_at')
        else:
            print('display error messages')

    # paginate products in given category
    paginator = Paginator(products, 3)  
    page = request.GET.get('page', 1) 
    page_content = paginator.get_page(page)


    # update tags from paginated products
    tags = set()
    for product in products:
        tags.update(product.tag.all())

    tags = list(tags)


    # generate dynamic products page navigation links
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