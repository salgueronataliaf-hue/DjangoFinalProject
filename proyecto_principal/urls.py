from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home  # Asumiendo que home está en accounts, o cámbialo a donde esté

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Vista de inicio
    path('accounts/', include('accounts.urls')),
    path('pages/', include('blog.urls')),
    path('mensajeria/', include('mensajeria.urls')),
]

# Esto permite ver las imágenes en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)