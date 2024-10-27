from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'store'

urlpatterns = [
    # main page
    path('', Indexview.as_view(), name='index'),
    # products listing by categories
    path('category/', category_products, name='products'),
    path('category/<slug:slug>/', category_products, name='products'),
    # product detailed page
    path('product/', ProductView.as_view(), name='product'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    # contacts page
    path('contact/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
]