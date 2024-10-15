from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('category/', categories, name='category'),
    path('category/<str:id>/products/', category_products, name='products'),
    path('product/<slug:slug>/', product_show, name='product'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)