from django.urls import path, include
from . import  views

app_name = 'calc'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
