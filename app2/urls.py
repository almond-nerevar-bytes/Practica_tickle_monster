from django.urls import path
from .views import lista_elementos_view

urlpatterns = [
    path('', lista_elementos_view, name='app2_lista')
]