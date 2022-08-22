#LO AGREGUE DE CHRISTIAN
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
#    path('login/', LoginView.as_view(template_name='ingresar.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.RegistrarUsuario.as_view(), name='Registro-Usuario'),

]