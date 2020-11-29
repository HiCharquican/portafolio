from django.urls import include, path, re_path
from rest_framework import routers
from portafolio import views
from rest_framework.authtoken import views as viewstoken
from .views import *

router = routers.DefaultRouter()
router.register(r'roles', views.GroupViewSet)
router.register(r'permisos', views.PermissionViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'tareas', views.TareaViewSet)
router.register(r'unidades', views.UnidadViewSet)
router.register(r'funciones', views.FuncionViewSet)
router.register(r'tareas_asignadas', views.TareaAsignadaViewSet)
router.register(r'reportes', views.ReporteViewSet)
router.register(r'indicacion_tarea', views.IndicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', viewstoken.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<token>/', views.CuttentToken),
    path('logout/<token>/', views.Logout),
    path('users', UserViewSet.as_view({'post': 'create'}), name="user_view")
]