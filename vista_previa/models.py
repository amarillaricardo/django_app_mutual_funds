from django.db import models

class Fondo(models.Model):
    nombre = models.CharField(max_length=200)	 
    tipo_de_inversión = models.CharField(max_length=200) 
    horizonte = models.CharField(max_length=200) 
    sociedad_gerente = models.CharField(max_length=200)	 
    sociedad_depositária = models.CharField(max_length=200) 
    region = models.CharField(max_length=200)	 
    cotizado_originalmente = models.CharField(max_length=200)	 
    calificacion = models.CharField(max_length=200) 
    fecha_de_calificacion = models.DateTimeField('Fecha de Calificacion')	 
    calificadora_de_riesgo = models.CharField(max_length=200)	 
    pais_sede = models.CharField(max_length=200) 
    tipo_de_activo = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    bolsa = models.CharField(max_length=200)
    codigo_cafci = models.CharField(max_length=200)
    comision_de_ingreso = models.CharField(max_length=200)
    honorarios_de_administración = models.CharField(max_length=200)
    otros = models.CharField(max_length=200)
    comision_de_egreso = models.CharField(max_length=200)
    comision_de_transferencia = models.CharField(max_length=200)
    gastos_ordinarios_de_gestión = models.CharField(max_length=200) 
    cobra_comision_por_perfomance = models.CharField(max_length=200)
    inversion_minima = models.CharField(max_length=200) 
    plazo_de_liquidacion = models.CharField(max_length=200)
    benchmark = models.CharField(max_length=200)	 
    duration = models.CharField(max_length=200)
    cuota_general = models.CharField(max_length=200)	 
    fecha_inicio_del_fondo = models.DateTimeField('Fecha de inicio del Fondo')
    fecha_publicacion = models.DateTimeField('Fecha de publicación')

    def __str__(self,):
        return self.nombre + '[' + self.codigo_cafci + ']'
    

    
