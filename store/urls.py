from django.urls import path
from djangostore import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('',products, name='products'),
    path('product/<str:id>',product_show, name='product-show'),
    path('categories',categories, name='categories'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
