"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from curriculum.views import verHome, verEstudios, verExperiencia, verHabilidades, verHobbies, verContacto

# En este archivo se configuran las URLs de la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', verHome, name='home'),
    path('estudios/', verEstudios, name='estudios'),
    path('experiencia/', verExperiencia, name='experiencia'),
    path('habilidades/', verHabilidades, name='habilidades'),
    path('hobbies/', verHobbies, name='hobbies'),
    path('contacto/', verContacto, name='contacto'),
]
