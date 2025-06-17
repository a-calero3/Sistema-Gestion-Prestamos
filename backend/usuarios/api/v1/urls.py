from django.urls import path
from .views import RegistroUserView

urlpatterns = [
    path('registro/', RegistroUserView.as_view(), name ='registro_usuario')
]