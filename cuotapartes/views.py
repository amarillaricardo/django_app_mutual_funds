from django.shortcuts import render
from django.http import HttpResponse
from cuotapartes.models import cotizaciones
from django.http.response import JsonResponse

def index(request):
    params = {}
    params['nombre_sitio'] = 'App de Fondos'
    return render(request,'cuotapartes/index.html',params)

def list_cotizaciones(_request):
    cotizaciones_de_vcp = list(cotizaciones.objects.values())
    data = {'cotizaciones_de_vcp':cotizaciones_de_vcp}
    return JsonResponse(data)