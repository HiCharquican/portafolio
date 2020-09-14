from rest_framework import viewsets, permissions as perm
from portafolio.serializers import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

### TOKEN
from django.http import JsonResponse
from rest_framework.response  import Response
from rest_framework  import status
from rest_framework.authtoken.models import Token

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

def CuttentToken(request, token):
    data = list(Token.objects.filter(pk=token).values())
    return JsonResponse(data, safe=False)
    
def Logout(request, token, format = None):
    if (Token.objects.filter(pk=token).values()):
        Token.objects.filter(pk=token).delete()
        return JsonResponse({'Correcto': 'Cierre de sesión completado'}, status=200)
    else:
        return JsonResponse({'Error': 'No hay usuario logeado'}, status=401)
    


