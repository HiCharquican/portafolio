from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['email', 'username',]

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Empresa)
admin.site.register(Tarea)
admin.site.register(RolUsuario)
admin.site.register(Unidad)
admin.site.register(Funcion)
admin.site.register(TareaAsignada)
admin.site.register(Post)
