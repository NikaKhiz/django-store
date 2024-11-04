from .models import Category, Product, ProductTag
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Count
from store.forms import ProductForm, SendEmailForm
from django.views import View
from django.core.cache import cache
from django.core import mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from userapp.models import CustomUser
from django.contrib import messages


class Indexview (View):

    def get(self, request):
        
        root_categories = cache.get('root_categories_cache')
        if root_categories is None:
            root_categories = Category.objects.filter(parent__isnull=True)
            cache.set('root_categories_cache', root_categories, 60 * 1)

        categories = cache.get('categories_cache')
        if categories is None:
            categories = root_categories.get_descendants(include_self=True)
            cache.set('categories_cache', categories, 60 * 1)

        products = cache.get('products_cache')
        if products is None:
            products = Product.objects.filter(category__in=categories).distinct().prefetch_related('tag')
            cache.set('products_cache', products, 60 * 1)

        context = {'root_categories': root_categories,'categories': categories, 'products': products}

        return render(request, 'index.html', context)


class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'
    paginate_by = 3 

    def get_queryset(self):

        slug = self.kwargs.get('slug')
        root_categories = cache.get('root_categories_cache')
        if root_categories is None:
            root_categories = Category.objects.filter(parent__isnull=True)
            cache.set('root_categories_cache', root_categories, 60 * 1)

        if slug:
            selected_category = get_object_or_404(Category, slug=slug)
            products = cache.get(f'selected_category_{slug}_products_cache')
            if products is None:
                products = Product.objects.filter(category=selected_category).distinct().prefetch_related('tag')
                cache.set(f'selected_category_{slug}_products_cache', products)

            self.categories = selected_category.get_children().annotate(product_count=Count('products'))
        else:
            self.categories = root_categories.annotate(product_count=Count('products'))
            
            products = cache.get('products_cache')
            if products is None:
                products = Product.objects.filter(category__in=self.categories).distinct().prefetch_related('tag')
                cache.set('products_cache', products, 60 * 1)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        context['slug'] = self.kwargs.get('slug')
        context['tags'] = ProductTag.objects.all().distinct()
        context['get_elided_page_range'] = context['paginator'].get_elided_page_range(
            self.request.GET.get(self.page_kwarg, 1)
            )

        # pass modified url to context for preserve filters on page switches
        get_url_copy = self.request.GET.copy()
        if get_url_copy.get('page'):
            get_url_copy.pop('page')
        context['copied_url'] = get_url_copy

        return context

    def get(self, request, *args, **kwargs):
        form = ProductForm(request.GET)
        if form.is_valid():
            queryset = self.get_queryset()

            product_name = form.cleaned_data['product_name']
            product_price = form.cleaned_data['product_price']
            tag = form.cleaned_data['product_tag']
            sort_option = form.cleaned_data['product_sort_list']

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

        else:
            return HttpResponse('form validation error', 400)


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
    

class ContactsView(FormView):
    success_url = '.'
    template_name = 'contacts.html'
    form_class = SendEmailForm

    #if submitted data is valid, send email and redirect to main page.
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        admin_users = CustomUser.objects.filter(is_superuser=True)
        admin_emails = admin_users.values_list('email', flat=True)

        try:
            mail.send_mail(
                'New user sent message.',
                cleaned_data.get('message'),
                cleaned_data.get('email'),
                admin_emails
            )
            messages.success(self.request, 'Your message has been sent succesfully! :)')
        except mail.BadHeaderError:
            return HttpResponse("Invalid header found.")
        
        return super().form_valid(form)
