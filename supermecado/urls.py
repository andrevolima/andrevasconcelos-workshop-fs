from django.contrib import admin
from django.urls import path, include
from supermercadosistema.views import clientesViewSet, fornecedoresViewSet, produtosViewSet, setoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', clientesViewSet, basename='clientess')
router.register('fornecedores', fornecedoresViewSet, basename='fornecedoress')
router.register('produtos', produtosViewSet, basename='produtoss')
router.register('setores', setoresViewSet, basename='setoress')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]