from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. URL de Administración de Django
    path('admin/', admin.site.urls),
    
    # 2. URLs de la aplicación principal (blog)
    # Asignamos el home ('') y el resto de rutas del blog
    path('', include('blog.urls')), 
    
    # 3. URLs de Autenticación y Cuentas (Registro, Login, Perfil)
    path('accounts/', include('accounts.urls')), 
    
    # 4. URLs de la aplicación de Mensajería (¡NUEVO!)
    # Se accede a la bandeja de entrada a través de /mensajeria/
    path('mensajeria/', include('mensajeria.urls')), 
] 
# Configuración para servir archivos estáticos (CSS, JS) y de medios (Imágenes)
# Solo se usa en modo DEBUG=True (desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)