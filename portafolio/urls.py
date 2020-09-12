from django.urls import include, path
from rest_framework import routers
from portafolio import views

router = routers.DefaultRouter()
router.register(r'roles', views.GroupViewSet)
router.register(r'permisos', views.PermissionViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'tareas', views.TareaViewSet)
router.register(r'unidades', views.UnidadViewSet)
router.register(r'funciones', views.FuncionViewSet)
router.register(r'tareas/asignadas', views.TareaAsignadaViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
]