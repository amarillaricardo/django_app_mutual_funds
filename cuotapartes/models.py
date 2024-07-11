from django.db import models
from vista_previa.models import Fondo

class cotizaciones(models.Model):
    monedas = (
        ('ARS',"ARS"),
        ('USD','USD'),
    )

    fondo_id = models.ForeignKey(Fondo,blank=False,null=True,on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField('Fecha')
    cuota = models.CharField(max_length=200,blank=False,null=True)
    patrimonio = models.CharField(max_length=200,blank=False,null=True)
    market_share = models.CharField(max_length=200,blank=False,null=True)
    cantidad_de_cuotas= models.CharField(max_length=200,blank=False,null=True)
    moneda = models.CharField(max_length=200,choices=monedas,default='ARS')

    class Meta:
        db_table = 'cotizacion_vcp'

