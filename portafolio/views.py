from rest_framework import viewsets, permissions as perm
from portafolio.serializers import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework import generics

### TOKEN
from django.http import JsonResponse
from rest_framework.response  import Response
from rest_framework  import status
from rest_framework.authtoken.models import Token

### PROCEDURES
from django.db import connection
import cx_Oracle, json

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [perm.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [perm.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [perm.IsAuthenticated]

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [perm.IsAuthenticated]

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [perm.IsAuthenticated]

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [perm.IsAuthenticated]

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer
    permission_classes = [perm.IsAuthenticated]

class TareaAsignadaViewSet(viewsets.ModelViewSet):
    queryset = TareaAsignada.objects.all()
    serializer_class = TareaAsignadaSerializer
    permission_classes = [perm.IsAuthenticated]

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [perm.IsAuthenticated]

class IndicacionViewSet(viewsets.ModelViewSet):
    queryset = IndicacionTarea.objects.all()
    serializer_class = IndicacionTareaSerializer
    permission_classes = [perm.IsAuthenticated]
    
    filter_fields = (['id_tarea',])

def CuttentToken(request, token):
    data = list(Token.objects.filter(pk=token).values())
    return JsonResponse(data, safe=False)

def Logout(request, token, format = None):
    if (Token.objects.filter(pk=token).values()):
        Token.objects.filter(pk=token).delete()
        return JsonResponse({'status': 200}, status=200)
    else:
        return JsonResponse({
            'status': 400
        }, status=400)

class UserViewSet(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def create(self, request):
        if request.method == 'POST':
            print (request)
            print (request)
            print (request)
            print (request)
            print (request)
            print (request)
            print (request)



class UserPaController():
    def crear_editar_usuario(self, id, username, password, nombre, apellido, email, telefono,direccion,region,rol_usuario_id, is_active, is_staff, is_superuser):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_CREAR_EDITAR_USUARIO', [username, password, nombre, apellido, email, telefono,direccion,region,rol_usuario_id, is_active, is_staff, is_superuser])
        return salida.getvalue()

        
manejadoraUsuario = UserPaController()

    


