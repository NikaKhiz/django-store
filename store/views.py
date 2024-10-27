from .models import Category, Product, ProductTag
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from store.forms import ProductForm
from django.views import View
from django.views.generic import DetailView


class Indexview (View):

    def get(self, request):
        root_categories = Category.objects.filter(parent__isnull=True)
        categories = root_categories.get_descendants(include_self=True)

        products = Product.objects.filter(category__in=categories).distinct().prefetch_related('tag')

        context = {'root_categories': root_categories,'categories': categories, 'products': products}

        return render(request, 'index.html', context)


def category_products(request, slug=None):
    # for displaying root categories in navigation
    root_categories = Category.objects.filter(parent__isnull=True)

    # get products according to given category if choosen, else from root categories
    if slug:
        selected_category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=selected_category).distinct().prefetch_related('tag')
        # get children categories from selected category object to display in template
        categories = selected_category.get_children().annotate(product_count=Count('products'))
    else:
        categories = root_categories.annotate(product_count=Count('products'))
        products = Product.objects.filter(category__in=categories).distinct().prefetch_related('tag')

    
    # get products of choosen categories 
    
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
    paginator = Paginator(products, 1)  
    page = request.GET.get('page', 1) 
    page_content = paginator.get_page(page)
    elided_page_range = paginator.get_elided_page_range(page_content.number, on_each_side=2, on_ends=2)

    # get product tags 
    tags = ProductTag.objects.filter(products__in=products).distinct()


    context = {
        'root_categories': root_categories,
        'categories': categories,
        'page_content': page_content,
        'tags' : tags,
        'slug': slug,
        'elided_page_range': elided_page_range,
        }

    return render(request, 'category_products.html', context)


# Product detailed page
class ProductView(DetailView):
    model = Product
    template_name= 'product.html'
    queryset= Product.objects.prefetch_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        context['category'] = product.category.annotate(product_count=Count('products')) 

        return context
    