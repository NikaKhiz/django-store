from django.urls import path
from .views import *

app_name = 'order'
urlpatterns = [
    path('cart/',order_create, name='cart'),
    path('checkout/',order_show, name='checkout'),
    path('cart_actions/<int:product_id>/', cart_actions, name='cart_actions'),
]
