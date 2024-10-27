from django.urls import path
from .views import *

app_name = 'order'
urlpatterns = [
    path('cart/',OrderCreateView.as_view(), name='cart'),
    path('checkout/',OrderShowView.as_view(), name='checkout'),
    path('cart_actions/<int:product_id>/', cart_actions, name='cart_actions'),
]
