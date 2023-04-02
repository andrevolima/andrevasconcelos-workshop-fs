from django.contrib import admin
from django.urls import path, include
from fabrica.views import clientesViewSet, colaboradoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', clientesViewSet, basename='clientess')
router.register('colaboradores', colaboradoresViewSet, basename='colaboradoress')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]

