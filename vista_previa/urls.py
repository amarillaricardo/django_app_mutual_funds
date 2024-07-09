
from django.urls import path
from vista_previa import views



urlpatterns = [
    path('', views.index,name = 'index'),
]
