from django.urls import path
from .views import home_app1

urlpatterns = [
    path('', home_app1, name='app1_home'),
]