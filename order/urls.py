from django.urls import path
from .views import *


urlpatterns = [
    path('order',order_create, name='order-create'),
    path('order/<str:id>',order_show, name='order-show')
]
