from django.urls import path
from djangostore import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    # for this moment we visit products page by default
    path('',product_index, name='product-index'),
    path('product/<str:id>',product_show, name='product-show'),
    path('categories',categories, name='categories'),
    path('products',products, name='products')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
