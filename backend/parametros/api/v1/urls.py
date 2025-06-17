from django.urls import path
from .views import CrearParametroView

urlpatterns = [
    path('crear/', CrearParametroView.as_view(), name = 'crear_parametro')
]