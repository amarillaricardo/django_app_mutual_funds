
from django.contrib import admin
from vista_previa.models import region,tipo_de_inversion,sociedad_depositaria,sociedad_gerente,Fondo


admin.site.register(region)
admin.site.register(tipo_de_inversion)
admin.site.register(sociedad_depositaria)
admin.site.register(sociedad_gerente)
admin.site.register(Fondo)
