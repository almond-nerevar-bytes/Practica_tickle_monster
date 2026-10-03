from django.urls import path
from .views import home_app3

urlpatterns = [
    path('', home_app3, name='app3_home')
]