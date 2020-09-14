from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario
from django.contrib.auth import get_user_model

class UsuarioCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario')

class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario')