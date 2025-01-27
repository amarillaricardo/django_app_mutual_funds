from django.contrib import admin
from datos_generales.models import benchmark
from datos_generales.models import cuota
from datos_generales.models import duration
from datos_generales.models import plazo_liquidacion
from datos_generales.models import tipo_de_activo
from datos_generales.models import pais_sede
from datos_generales.models import calificacion
from datos_generales.models import calificadora_de_riesgo
from datos_generales.models import moneda
from datos_generales.models import horizonte
from datos_generales.models import region
from datos_generales.models import tipo_de_inversion
from datos_generales.models import sociedad_depositaria
from datos_generales.models import sociedad_gerente
from datos_generales.models import Fondo

 

class FondoInline(admin.TabularInline):
    model = Fondo
    extra = 0

class sociedad_gerenteAdmin(admin.ModelAdmin):
    inlines = [FondoInline]

class FondoAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Datos Generales",
            {
                "fields":[
                    'nombre','clase','codigo_economatica','tipo_de_inversión','horizonte',
                    'sociedad_gerente','sociedad_depositária','region','cotizado_originalmente',
                    'calificacion','fecha_de_calificacion','calificadora_de_riesgo','pais_sede',
                    'tipo_de_activo','estado','bolsa','codigo_cafci'
                ]
            },
        ),
        (
            "Comisiones",
         {
             "fields":[
                'comision_de_ingreso','honorarios_de_administración','otros','comision_de_egreso',
                'comision_de_transferencia','gastos_ordinarios_de_gestión','cobra_comision_por_perfomance'
            ]
         },
        ),
        (
            "Otros",
            {
                 "fields":[
                    'inversion_minima','plazo_de_liquidacion','benchmark','duration',
                    'cuota_general','fecha_inicio_del_fondo','fecha_publicacion'
                ]
            },
        ),
    ]
    list_display = ['nombre','sociedad_gerente','tipo_de_inversión','cotizado_originalmente','tipo_de_estado','fecha_publicacion','detalles']
    ordering = ['-fecha_publicacion']
    list_filter = ('nombre','sociedad_gerente','tipo_de_inversión','cotizado_originalmente','fecha_publicacion',)
    search_fields = ('nombre',)
    list_display_links = ('nombre','sociedad_gerente')

    @admin.display(description='Detalles')
    def detalles(self,obj):
        return '%s - Clase %s' % (obj.nombre,obj.clase)



admin.site.register(benchmark)
admin.site.register(cuota)
admin.site.register(duration)
admin.site.register(plazo_liquidacion)
admin.site.register(tipo_de_activo)
admin.site.register(pais_sede)
admin.site.register(calificacion)
admin.site.register(calificadora_de_riesgo)
admin.site.register(moneda)
admin.site.register(horizonte)
admin.site.register(region)
admin.site.register(tipo_de_inversion)
admin.site.register(sociedad_depositaria)
admin.site.register(sociedad_gerente,sociedad_gerenteAdmin)
admin.site.register(Fondo,FondoAdmin)
#admin.site.register(sociedad_gerente)
