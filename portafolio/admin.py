from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = UserAdmin
    list_display = ['username', 'password', 'rut','nombre', 'apellido', 'email', 'telefono', 'direccion', 'region', 'rol_usuario']

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Empresa)
admin.site.register(Tarea)
admin.site.register(Unidad)
admin.site.register(Funcion)
admin.site.register(TareaAsignada)
admin.site.register(Post)
