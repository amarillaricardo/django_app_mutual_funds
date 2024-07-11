
from django.urls import path
from datos_generales import views



urlpatterns = [
    path('', views.index,name = 'index'),
]
