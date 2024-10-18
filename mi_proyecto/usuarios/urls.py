# usuarios/urls.py
from django.urls import path
from .views import crear_usuario

urlpatterns = [
    path('crearusuario/', crear_usuario, name='crear_usuario'),
]

