from rest_framework import serializers
from .models import CadastroUnidadeMedida, CadastroFabricante, CadastroEquipamento, CadastroSensor, CadastroTipoSensor, InstalacaoSensor
from .models import CadastroLeitura

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroUnidadeMedida
        fields = '__all__'

class CadastroFabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroFabricante
        fields = '__all__'

class CadastroEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroEquipamento
        fields = '__all__'

class CadastroSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroSensor
        fields = '__all__'

class CadastroTipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroTipoSensor
        fields = '__all__'

class InstalacaoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalacaoSensor
        fields = '__all__'

class CadastroLeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroLeitura
        fields = '__all__'