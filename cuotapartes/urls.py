
from django.urls import path
from cuotapartes import views



urlpatterns = [
    path('', views.index,name = 'index'),
]
