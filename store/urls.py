from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    # main page
    path('', index, name='index'),
    # products listing 
    path('category/<slug:slug>/', category_products, name='products'),
    # product detailed
    path('product/<slug:slug>/', product_show, name='product'),
    # contact page
    path('contact/', contacts, name='contactsgit add store'),
]