from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', include('store.urls', namespace='store')),
    path('order/', include('order.urls', namespace='order')),
    path('user/', include('userapp.urls', namespace='user')),
    path('admin/', admin.site.urls, name='admin'),
    prefix_default_language=False
) + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)