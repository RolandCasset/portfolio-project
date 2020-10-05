from django.urls import path
from .import views

urlpatterns = [
    path('', views.imgSources, name='imgSources'),
]
