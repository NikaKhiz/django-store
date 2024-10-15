from django.urls import path
from .views import *


urlpatterns = [
    path('category/', categories, name='category'),
    path('category/<str:id>/products/', category_products, name='products'),
    path('product/<slug:slug>/', product_show, name='product'),
]
