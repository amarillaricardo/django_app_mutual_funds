from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {}
    params['nombre_sitio'] = 'App de Fondos'
    return render(request,'vista_previa/index.html',params)