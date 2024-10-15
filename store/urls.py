from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', categories, name='category'),
    path('<str:category_id>/products/', category_products, name='products'),
    path('<str:category_id>/products/product/<slug:slug>/', product_show, name='product'),
]