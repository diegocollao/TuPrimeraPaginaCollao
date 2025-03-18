from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
