from django.urls import path
from . import views

#path('adddata', views.addFromExel, name="addfromexel")    > To Add Data From Excel
urlpatterns = [
    path('', views.index),
    path('read/<int:pk>', views.read, name="read"),

]