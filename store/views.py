from .models import Category, Product, ProductTag
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count
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

class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'
    paginate_by = 1  

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        root_categories = Category.objects.filter(parent__isnull=True)

        if slug:
            selected_category = get_object_or_404(Category, slug=slug)
            products = Product.objects.filter(category=selected_category).distinct().prefetch_related('tag')
            self.categories = selected_category.get_children().annotate(product_count=Count('products'))
        else:
            self.categories = root_categories.annotate(product_count=Count('products'))
            products = Product.objects.filter(category__in=self.categories).distinct().prefetch_related('tag')

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['root_categories'] = Category.objects.filter(parent__isnull=True)
        context['categories'] = self.categories
        context['slug'] = self.kwargs.get('slug')
        context['tags'] = ProductTag.objects.all().distinct()
        context['get_elided_page_range'] = context['paginator'].get_elided_page_range(
            self.request.GET.get(self.page_kwarg, 1)
            )

        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = request.POST.get('product_name')
            product_price = request.POST.get('product_price')
            tag = request.POST.get('product_tag')
            sort_option = request.POST.get('sort_list')
            
            queryset = self.get_queryset()
            if product_name:
                queryset = queryset.filter(name__icontains=product_name)
            if product_price:
                queryset = queryset.filter(price__lte=product_price)
            if tag:
                queryset = queryset.filter(tag__name__icontains=tag)

            if sort_option == 'price_up':
                queryset = queryset.order_by('price')
            elif sort_option == 'price_down':
                queryset = queryset.order_by('-price')
            elif sort_option == 'created_at':
                queryset = queryset.order_by('-created_at')

            self.object_list = queryset
            context = self.get_context_data()
            return self.render_to_response(context)

        return self.get(request, *args, **kwargs)


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
    