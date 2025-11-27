# proyecto_principal/urls.py
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
    # NUEVAS RUTAS DE AUTENTICACIÓN
    path('accounts/', include('accounts.urls')),
]

# Configuración para servir archivos media (imágenes) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
