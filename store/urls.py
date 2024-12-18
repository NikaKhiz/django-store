from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

app_name = 'store'

urlpatterns = [
    # main page
    path('', Indexview.as_view(), name='index'),
    # products listing by categories
    path('category/', CategoryProductsView.as_view(), name='products'),
    path('category/<slug:slug>/', CategoryProductsView.as_view(), name='products'),
    # product detailed page
    path('product/', ProductView.as_view(), name='product'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    # contacts page
    path('contact/', ContactsView.as_view(template_name='contacts.html'), name='contacts'),
]