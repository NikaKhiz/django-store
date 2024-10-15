from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('category/', include('store.urls', namespace='store')),
    path('order/', include('order.urls', namespace='order')),
    path('admin/', admin.site.urls, name='admin'),
    path('', RedirectView.as_view(url='admin/', permanent=False))
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
