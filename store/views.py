from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg
from django.core.paginator import Paginator


def index(request):
    context = {'categories': []}
    return render(request, 'index.html', context)


def category_products(request, slug):
    context = {'products': []}
    return render(request, 'category_products.html', context)


# Product detailed page
def product_show(request, category_id, slug):
    category = get_object_or_404(Category, id=category_id) 
    product = Product.objects.get(category=category, slug=slug)

    context = {'product' : product, 'category_id': category_id}

    return render(request, 'product.html', context)


def contacts(request):
    context = {'contacts': []}
    return render(request, 'contacts.html', context)
