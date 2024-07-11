from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

class Datosusuarios(models.Model):
    
    paises = (
        ("Argentina","Argentina"),
        ("Brasil","Brasil"),
        ("Uruguay","Uruguay"),
        ("Chile","Chile"),
        ("Bolivia","Bolivia"),
        ("Paraguay","Paraguay"),
        ("Peru","Peru"),
        ("Otro","Otro"),
    )
    provincias = (
        ('Buenos Aires','Buenos Aires'),
        ('Ciudad Autónoma de Buenos Aires','Ciudad Autónoma de Buenos Aires'),
        ('Catamarca','Catamarca'),
        ('Chaco','Chaco'),
        ('Chubut','Chubut'),
        ('Córdoba','Córdoba'),
        ('Corrientes','Corrientes'),
        ('Entre Ríos','Entre Ríos'),
        ('Formosa','Formosa'),
        ('Jujuy','Jujuy'),
        ('La Pampa','La Pampa'),
        ('La Rioja','La Rioja'),
        ('Mendoza','Mendoza'),
        ('Misiones','Misiones'),
        ('Neuquén','Neuquén'),
        ('Río Negro','Río Negro'),
        ('Salta','Salta'),
        ('San Juan','San Juan'),
        ('San Luis','San Luis'),
        ('Santa Cruz','Santa Cruz'),
        ('Santa Fe','Santa Fe'),
        ('Santiago del Estero','Santiago del Estero'),
        ('Tierra del Fuego','Tierra del Fuego'),
        ('Tucumán','Tucumán'),
        ('Otro','Otro')

    )

    
    usuario = models.ForeignKey(User,blank=False,null=True,on_delete=models.CASCADE)
    nombre  = models.CharField(max_length=200)
    apellido  = models.CharField(max_length=200)
    fecha_nacimiento  = models.DateField(blank=True,null=True)
    pais = models.CharField(max_length=200,choices=paises,default="Argentina") 
    provincia = models.CharField(max_length=200,choices=provincias,default="Buenos Aires")
    ciudad  = models.CharField(max_length=200,blank=True)
    domicilio  = models.CharField(max_length=200,blank=True)
    codigo_postal  = models.CharField(max_length=200,blank=True)
    telefono  = models.CharField(max_length=200,blank=True)
    celular  = models.CharField(max_length=200,blank=True)
    documento  = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.usuario.username