"""fund_uocra_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import About, Category, Contact, Index, Search_Result, Single_Post

#ESTO LO AGREGUE DE ABI from .views import Index, galeria, basic, full, sidebar_left, sidebar_right 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name = 'inicio'),
    path('index/', Index, name = 'index'),
    path('noticia/', include ('apps.noticia.urls') ),
    path('ingresar/', include ('apps.usuario.urls'), name='ingresar'),
    path('accounts/', include('django.contrib.auth.urls')),
#   path('comentario/', include ('apps.comentario.urls') ),
# LO QUE SIGUE LO AGREGUE DE ABI
    path('about/', About, name='about'),
    path('category/', Category, name='category'),
    path('contact/', Contact, name='contact'), 
    path('search-result/', Search_Result, name='search-result'),
    path('single-post/', Single_Post, name='single-post'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
