from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

import cx_Oracle
from django.db import connection


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'url', 'username', 'password', 'rut','nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario','is_active', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.rut = validated_data.get('rut', instance.rut)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.email = validated_data.get('email', instance.email)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.region = validated_data.get('region', instance.region)
        instance.rol_usuario = validated_data.get('rol_usuario', instance.rol_usuario)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'url', 'nombre', 'descripcion']

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['url', 'id', 'nombre', 'descripcion', 'empresa']

class FuncionSerializer(serializers.ModelSerializer):
    nombre_tarea = serializers.ReadOnlyField(source='tarea.nombre')
    nombre_usuario = serializers.ReadOnlyField(source='usuario.username')
    nombre_unidad = serializers.ReadOnlyField(source='unidad.nombre')
    class Meta:
        model = Funcion
        fields = ['url', 'id', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'porcentaje_realizacion', 'tarea', 'nombre_tarea', 'usuario', 'nombre_usuario', 'unidad', 'nombre_unidad']

class TareaAsignadaSerializer(serializers.ModelSerializer):
    nombre_tarea = serializers.ReadOnlyField(source='tarea.nombre')
    descripcion_tarea = serializers.ReadOnlyField(source='tarea.descripcion')
    nombre_usuario = serializers.ReadOnlyField(source='usuario.username')
    nombre_funcion = serializers.ReadOnlyField(source='funcion.nombre')

    class Meta:
        model = TareaAsignada
        fields = ['id', 'nombre_tarea', 'descripcion_tarea', 'url', 'fecha_inicio', 'fecha_termino', 'terminada', 'tarea', 'nombre_tarea', 'usuario', 'nombre_usuario', 'funcion', 'nombre_funcion']


