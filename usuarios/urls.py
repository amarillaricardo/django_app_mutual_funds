
from django.urls import path
from usuarios import views



urlpatterns = [
    path('', views.index,name = 'index'),
]
