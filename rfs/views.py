from .serializers import UnidadeMedidaSerializer, CadastroFabricanteSerializer, CadastroEquipamentoSerializer, CadastroSensorSerializer, CadastroTipoSensorSerializer, InstalacaoSensorSerializer
from .serializers import CadastroLeituraSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CadastroUnidadeMedida, CadastroEquipamento, CadastroFabricante, CadastroSensor, CadastroTipoSensor, InstalacaoSensor
from .models import CadastroLeitura
from  app.permissions import GlobalDefaultPermissionClass
from django import forms
from django.core.exceptions import ValidationError
## view de listar e criar Unidade Medida
class UnidadeMedidaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroUnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

## view de editar e apagar Unidade Medida
class UnidadeMedidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroUnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer
## view de listar e criar Fabricante
class FabricanteView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroFabricante.objects.all()
    serializer_class = CadastroFabricanteSerializer

## view de editar e apagar Fabricante
class FabricanteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroFabricante.objects.all()
    serializer_class = CadastroFabricanteSerializer
## view de listar e criar Sensor
class SensorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroSensor.objects.all()
    serializer_class = CadastroSensorSerializer

## view de editar e apagar Sensor
class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroSensor.objects.all()
    serializer_class = CadastroSensorSerializer
## view de listar e criar Equipamento
class EquipamentoView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroEquipamento.objects.all()
    serializer_class = CadastroEquipamentoSerializer

## view de editar e apagar Equipamento    
class EquipamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroEquipamento.objects.all()
    serializer_class = CadastroEquipamentoSerializer

## view de listar e criar Tipo Sensor
class TipoSensorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroTipoSensor.objects.all()
    serializer_class = CadastroTipoSensorSerializer

## view de editar e apagar Tipo Sensor
class TipoSensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroTipoSensor.objects.all()
    serializer_class = CadastroTipoSensorSerializer

class InstalacaoSensorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = InstalacaoSensor.objects.all()
    serializer_class = InstalacaoSensorSerializer

class InstalacaoSensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = InstalacaoSensor.objects.all()
    serializer_class = InstalacaoSensorSerializer

class CadastroLeituraView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroLeitura.objects.all()
    serializer_class = CadastroLeituraSerializer

class LeituraRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = CadastroLeitura.objects.all()
    serializer_class = CadastroLeituraSerializer
