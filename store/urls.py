from django.urls import path
from .views import *


urlpatterns = [
    path('',products, name='products'),
    path('product/<str:id>',product_show, name='product-show'),
    path('categories',categories, name='categories'),
]
