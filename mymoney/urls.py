from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.apiOverview, name='api-response'),
    path('api/', views.apiOverview, name='api-response'),
    path('api/expense/', views.expenseList, name='expenses_list'),

]