from rest_framework import serializers
from .models import *


class RolUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RolUsuario
        fields = ['url', 'nombre', 'descripcion']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username', 'rut', 'nombre', 'apellido', 'email', 'direccion', 'region', 'rol_usuario']

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ['url', 'rut', 'nombre', 'telefono', 'email', 'direccion', 'region']

class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ['url', 'nombre', 'descripcion']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username', 'email']

class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ['url', 'nombre', 'descripcion', 'empresa']

class FuncionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcion
        fields = ['url', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'porcentaje_realizacion', 'creador', 'unidad']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username', 'email']

class TareaAsignadaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TareaAsignada
        fields = ['url', 'fecha_inicio', 'fecha_termino', 'terminada', 'tarea', 'asigando', 'funcion']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text','created_date','published_date']