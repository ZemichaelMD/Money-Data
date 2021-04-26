from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('read/<int:pk>', views.read, name="read")
]