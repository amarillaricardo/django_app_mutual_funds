from django.db import models


class sociedad_gerente(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return '%s'% self.nombre
class sociedad_depositaria(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return '%s'% self.nombre

class tipo_de_inversion(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return '%s'% self.nombre

class region(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre

class horizonte(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
    
class moneda(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre

class calificacion(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
    
class calificadora_de_riesgo(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre

class pais_sede(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre

class tipo_de_activo(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre


class cuota(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
class benchmark(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
class benchmark(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
class plazo_liquidacion(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre
class duration(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_interno =models.CharField(max_length=200)
    def __str__(self,):
        return self.nombre

class Fondo(models.Model):
    nombre = models.CharField(max_length=200)
    clase =	models.CharField(blank=True,max_length=200,default="")
    codigo_economatica = models.CharField(blank=True,max_length=200,default="") 
    tipo_de_inversión = models.ForeignKey(tipo_de_inversion, on_delete=models.CASCADE)
    horizonte = models.ForeignKey(horizonte, on_delete=models.CASCADE)
    sociedad_gerente = models.ForeignKey(sociedad_gerente, on_delete=models.CASCADE)
    sociedad_depositária = models.ForeignKey(sociedad_depositaria, on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE) 
    cotizado_originalmente = models.ForeignKey(moneda, on_delete=models.CASCADE) 
    calificacion = models.ForeignKey(calificacion, on_delete=models.CASCADE) 
    fecha_de_calificacion = models.DateField('Fecha de Calificacion')	 
    calificadora_de_riesgo = models.ForeignKey(calificadora_de_riesgo, on_delete=models.CASCADE) 	 
    pais_sede = models.ForeignKey(pais_sede, on_delete=models.CASCADE)
    tipo_de_activo = models.ForeignKey(tipo_de_activo, on_delete=models.CASCADE)
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
    plazo_de_liquidacion = models.ForeignKey(plazo_liquidacion, on_delete=models.CASCADE)
    benchmark = models.ForeignKey(benchmark, on_delete=models.CASCADE) 
    duration = models.ForeignKey(duration, on_delete=models.CASCADE)
    cuota_general = models.ForeignKey(cuota, on_delete=models.CASCADE)	 
    fecha_inicio_del_fondo = models.DateField('Fecha de inicio del Fondo')
    fecha_publicacion = models.DateTimeField('Fecha de publicación')


    def __str__(self,):
        return self.nombre + ' [' + self.codigo_cafci + ']'
    


