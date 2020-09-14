from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password



from rest_framework.authtoken.models import Token

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
        fields = ['url', 'username', 'password', 'rut','nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario','is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).create(validated_data)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['url', 'nombre', 'descripcion']

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['url', 'nombre', 'descripcion', 'empresa']

class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = ['url', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'porcentaje_realizacion', 'creador', 'unidad']

class TareaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaAsignada
        fields = ['url', 'fecha_inicio', 'fecha_termino', 'terminada', 'tarea', 'asigando', 'funcion']


