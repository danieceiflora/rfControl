
from django.contrib import admin
from django.urls import path, include
from rfs.views import UnidadeMedidaView, FabricanteView, SensorView, EquipamentoView, TipoSensorView, UnidadeMedidaRetrieveUpdateDestroyView, FabricanteRetrieveUpdateDestroyView
from rfs.views import SensorRetrieveUpdateDestroyView, EquipamentoRetrieveUpdateDestroyView, TipoSensorRetrieveUpdateDestroyView, InstalacaoSensorView, InstalacaoSensorRetrieveUpdateDestroyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    

    ##rotas api , v1, listar e criar
    path('api/v1/unidade-medida/', UnidadeMedidaView.as_view(), name='unidade-medida'),
    path('api/v1/fabricante/', FabricanteView.as_view(), name='fabricante'),
    path('api/v1/sensor/', SensorView.as_view(), name='sensor'),
    path('api/v1/equipamento/', EquipamentoView.as_view(), name='equipamento'),
    path('api/v1/tipo-sensor/', TipoSensorView.as_view(), name='tipo-sensor'),
    path('api/v1/instalacao-sensor/', InstalacaoSensorView.as_view(), name='instalacao-sensor'),

    ## rotas api, v1 editar e apagar.
    path('api/v1/unidade-medida/<int:pk>', UnidadeMedidaRetrieveUpdateDestroyView.as_view(), name='unidade-medida'),
    path('api/v1/fabricante/<int:pk>', FabricanteRetrieveUpdateDestroyView.as_view(), name='fabricante'),
    path('api/v1/sensor/<int:pk>', SensorRetrieveUpdateDestroyView.as_view(), name='sensor'),
    path('api/v1/equipamento/<int:pk>', EquipamentoRetrieveUpdateDestroyView.as_view(), name='equipamento'),
    path('api/v1/tipo-sensor/<int:pk>', TipoSensorRetrieveUpdateDestroyView.as_view(), name='tipo-sensor'),
    path('api/v1/instalacao-sensor/<int:pk>', InstalacaoSensorRetrieveUpdateDestroyView.as_view(), name='instalacao-sensor'),

    path('api/v1/', include('authentication.urls')),
    
    # Rota para o esquema JSON
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI para visualização da documentação
    path('api/v1/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc para uma documentação alternativa
    path('api/v1/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]
