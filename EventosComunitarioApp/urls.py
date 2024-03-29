"""
URL configuration for EventosComunitarioApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_bienvenida, name='pagina_bienvenida'),
    path('calendario/', views.calendario_eventos, name='calendario_eventos'),
    path('registro-evento/', views.registro_eventos, name='registro_evento'),
    path('buscar_evento/', views.buscar_eventos, name='buscar_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:evento_id>/registrar_asistencia/', views.registrar_asistencia, name='registrar_asistencia'),
]

