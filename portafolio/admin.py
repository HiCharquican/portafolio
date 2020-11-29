from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = UserAdmin
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Empresa)
admin.site.register(Tarea)
admin.site.register(Unidad)
admin.site.register(Funcion)
admin.site.register(TareaAsignada)
admin.site.register(IndicacionTarea)
