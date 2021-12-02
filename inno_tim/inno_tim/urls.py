from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from inno_tim import settings

urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),
    path('user/', include('authapp.urls', namespace='authapp')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
