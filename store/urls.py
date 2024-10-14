from django.urls import path
from .views import *


urlpatterns = [
    path('category',categories, name='categories'),
    path('category/<str:id>/products',categories, name='category'),
    path('product',product_show, name='product'),
]
