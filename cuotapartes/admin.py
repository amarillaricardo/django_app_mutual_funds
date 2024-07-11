from django.contrib import admin
from cuotapartes.models import cotizaciones

class cotizacionesAdmin(admin.ModelAdmin):
    list_display = ['fondo_id','fecha_cotizacion','cuota','patrimonio','market_share','cantidad_de_cuotas','moneda']
    ordering = ['-fecha_cotizacion']
    list_filter = ('fondo_id','fecha_cotizacion','cuota','patrimonio','market_share','cantidad_de_cuotas','moneda',)
    search_fields = ('fondo_id',)




admin.site.register(cotizaciones,cotizacionesAdmin)