from django.urls import path
from .views import *

app_name = 'order'
urlpatterns = [
    path('cart/',order_create, name='cart'),
    path('checkout/',order_show, name='checkout')
]
