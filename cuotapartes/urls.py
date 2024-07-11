
from django.urls import path
from cuotapartes import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('list_cotizaciones/', views.list_cotizaciones,name = 'list_cotizaciones'),
]
