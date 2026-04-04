from django.urls import path
from . import views

urlpatterns = [
    path('', views.temperature_converter, name='converter'),
]