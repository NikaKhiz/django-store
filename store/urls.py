from django.urls import path
from .views import *


urlpatterns = [
    path('categories',categories, name='categories'),
    path('category/<str:id>/products',categories, name='category'),
    path('product',product_show, name='product'),
]
