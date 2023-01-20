"""roupas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from meuapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('roupas/crud', views.crud_Roupas, name='crud_Roupas'),
    path('roupas/listar', views.listar_Roupas, name='listar_Roupas'),
    path('roupa/c/', views.criar_Roupas, name='criar_Roupas'),
    path('roupa/e/<int:pk>', views.editar_Roupas, name='editar_Roupas'),
    path('roupa/d/<int:pk>', views.delete_Roupas, name='delete_Roupas'),
    path('consulta/', views.consulta, name='consulta'),
    path('sobre/', views.sobre, name='sobre'),
]
