
from django.contrib import admin
from vista_previa.models import benchmark,cuota,duration,plazo_liquidacion,tipo_de_activo,pais_sede,calificacion,calificadora_de_riesgo,moneda,horizonte,region,tipo_de_inversion,sociedad_depositaria,sociedad_gerente,Fondo

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
admin.site.register(sociedad_gerente)
admin.site.register(Fondo)
