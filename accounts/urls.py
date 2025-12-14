# accounts/urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView # LogoutView es una CBV
from . import views # Importamos el módulo completo

urlpatterns = [
    # Ruta inicial para la app accounts
    path('', views.home, name='home'),
    
    # Rutas de Cuentas (Aplicando el prefijo 'views.')
    path('register/', views.register_request, name='register'),
    path('about/', views.about, name='about'),
    path('login/', views.login_request, name='login'),
    
    # Logout: Se usa la clase LogoutView, que es externa
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html', next_page='home'), name='logout'), 
    
    # Rutas de Perfil
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.editar_perfil, name='profile_edit'),
    path('profile/password/', views.change_password, name='change_password'),
]