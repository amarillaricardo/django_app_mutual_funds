
from django.contrib import admin
from vista_previa.models import benchmark
from vista_previa.models import cuota
from vista_previa.models import duration
from vista_previa.models import plazo_liquidacion
from vista_previa.models import tipo_de_activo
from vista_previa.models import pais_sede
from vista_previa.models import calificacion
from vista_previa.models import calificadora_de_riesgo
from vista_previa.models import moneda
from vista_previa.models import horizonte
from vista_previa.models import region
from vista_previa.models import tipo_de_inversion
from vista_previa.models import sociedad_depositaria
from vista_previa.models import sociedad_gerente
from vista_previa.models import Fondo


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
