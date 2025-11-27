# accounts/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la autenticación
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'), 
]