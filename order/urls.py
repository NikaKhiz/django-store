from django.urls import path
from .views import *

app_name = 'order'
urlpatterns = [
    path('',order_create, name='order-create'),
    path('<str:id>',order_show, name='order-show')
]
