from django.urls import path
from .views import *


urlpatterns = [
    # for this moment we visit products page by default
    path('',product_index, name='product-index'),
    path('product/<str:id>',product_show, name='product-show')
]
