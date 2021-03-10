from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import django.conf.urls.i18n

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('chart.urls', namespace='chart'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
