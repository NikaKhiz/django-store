from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, F, Sum, Max, Min, Avg
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

categories = []
for _ in range(6):
    categories.append(
        {
            'title': 'Fruits',
            'slug': 'fruits',
            'description':'Lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod te incididunt',
            'image':'img/fruite-item-1.jpg'
        }
    )

def index(request):
    
    context = {'categories': categories}
    return render(request, 'index.html', context)


def category_products(request, slug='fruits'):
    context = {'products': products}
    return render(request, 'category_products.html', context)


# Product detailed page
def product_show(request, slug='apple'):
    
    context = {'product' : products[3], }

    return render(request, 'product.html', context)


# contacts page
def contact(request):
    return render(request, 'contacts.html')