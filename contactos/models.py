from django.db import models

# Create your models here.

class ContactoClientes(models.Model):
    nombre = models.CharField(max_length= 100)
    email = models.EmailField()
    mensaje = models.CharField(max_length=500)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField
    esContactado = models.BooleanField(default=False)

class Personas(models.Model):
    nombres = models.CharField(max_length= 200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    estaActivo =  models.BooleanField(default=True)

class TelefonoPersona(models.Model):
    telefono = models.CharField(max_length=15)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, null=False, blank=False)
    estaActivo = models.BooleanField(default=True)

class CorreoPersona(models.Model):
    email = models.EmailField()
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, null=False, blank=False)
    estaActivo = models.BooleanField(default=True)
