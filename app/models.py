from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class campana(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    organizacion = models.CharField(blank=True, max_length=100, verbose_name='organizacion')
    fecha = models.DateField()
    ubicacion = models.CharField(blank=True, max_length=100, verbose_name='ubicacion')
    celular = models.IntegerField(blank=True, verbose_name='celular')
    ciudad = models.CharField(blank=True, max_length=100, verbose_name='ciudad')
    correo = models.CharField(blank=True, max_length=100, verbose_name='correo')

    class Meta():
        verbose_name = "campana"
        verbose_name_plural = "campanas"

    def __str__(self):
        return self.nombre
   
    
class hospital(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    ciudad = models.CharField(blank=True, max_length=100, verbose_name='ciudad')
    celular = models.IntegerField(blank=True, verbose_name='celular')
    ubicacion = models.CharField(blank=True, max_length=100, verbose_name='ubicacion') 
    correo = models.CharField(blank=True, max_length=100, verbose_name='correo')

    class Meta():
        verbose_name = "hospital"
        verbose_name_plural = "hospitales"

    def __str__(self):
        return self.nombre
    
   
class incentivo(models.Model):
    nombre = models.CharField(blank=True, max_length=100, verbose_name='nombre')
    empresa = models.CharField(blank=True, max_length=100, verbose_name='empresa')
    fecha = models.DateField()
    tipo = models.CharField(blank=True, max_length=100, verbose_name='tipo')
    celular = models.IntegerField(blank=True, verbose_name='celular')
    correo = models.CharField(blank=True, max_length=100, verbose_name='correo')

    class Meta():
        verbose_name = "incentivo"
        verbose_name_plural = "incentivos"

    def __str__(self):
        return self.nombre
        

class datos_usuario(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    documento = models.CharField(blank=True, max_length=100, verbose_name='documento')
    numDocumento = models.IntegerField(blank=True, verbose_name='numDocumento')
    grupo = models.CharField(blank=True, max_length=100, verbose_name='grupo')
    rh = models.CharField(blank=True, max_length=100, verbose_name='rh')
    fecha = models.DateField()
    genero = models.CharField(blank=True, max_length=100, verbose_name='genero')
    ciudad = models.CharField(blank=True, max_length=100, verbose_name='ciudad')
    celular = models.IntegerField(blank=True, verbose_name='celular')

    class Meta():
        verbose_name = "datos_usuario"
        verbose_name_plural = "datos_usuarios"

    def __str__(self):
        return self.grupo
