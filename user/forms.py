from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    rut = forms.CharField(max_length=50)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=50)
    region = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'rut', 'nombres', 'apellidos',
                  'telefono', 'region', 'direccion', 'password1', 'password2']
