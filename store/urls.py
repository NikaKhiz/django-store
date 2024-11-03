from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

app_name = 'store'

urlpatterns = [
    # main page
    path('', cache_page(60 * 1)(Indexview.as_view()), name='index'),
    # products listing by categories
    path('category/', cache_page(60 * 1)(CategoryProductsView.as_view()), name='products'),
    path('category/<slug:slug>/', cache_page(60 * 1)(CategoryProductsView.as_view()), name='products'),
    # product detailed page
    path('product/', ProductView.as_view(), name='product'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    # contacts page
    path('contact/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
]