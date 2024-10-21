from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    # main page
    path('', index, name='index'),
    # products listing by categories
    path('category/', category_products, name='products'),
    path('category/<slug:slug>/', category_products, name='products'),
    # product detailed page
    path('product/', product_show, name='product'),
    path('product/<slug:slug>/', product_show, name='product'),
]