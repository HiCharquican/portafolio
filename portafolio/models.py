from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group
from django.contrib import admin

class Usuario(AbstractUser):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    telefono = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    rol_usuario = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username


class Empresa(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Funcion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    porcentaje_realizacion = models.IntegerField()
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, blank=True, null=True)
    unidad = models.ForeignKey('Unidad', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class IndicacionTarea(models.Model):
    terminada = models.BooleanField(default=False)
    indicaciones = models.CharField(max_length=256, blank=True, null=True)
    id_tarea = models.ForeignKey('TareaAsignada', on_delete=models.CASCADE, blank=True, null=True)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
            return self.indicaciones

class TareaAsignada(models.Model):
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    terminada = models.BooleanField(default=False)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, blank=True, null=True)
    funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE, blank=True, null=True)
    indicacion = models.ManyToManyField(IndicacionTarea, blank=True)

    def __str__(self):
        return self.tarea.nombre

class Reporte(models.Model):
    fecha_reporte = models.DateField(auto_now=True)
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)
    tarea = models.ForeignKey('TareaAsignada', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre
