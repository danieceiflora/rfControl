from django.db import models
from rfs.validators import validar_cnpj, validar_telefone
from django.core.exceptions import ValidationError
import re

class CadastroUnidadeMedida(models.Model):
    
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    idOrigem = models.CharField(max_length=20, blank=True, null=True, verbose_name='Id de Origem')
    simbolo = models.CharField(max_length=20, verbose_name='Símbolo')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class CadastroFabricante(models.Model):
    
    nome = models.CharField(max_length=200, verbose_name='Nome')
    idOrigem = models.CharField(max_length=20, blank=True, null=True, verbose_name='Id de Origem')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', unique=True, validators=[validar_cnpj])
    telefone = models.CharField(max_length=15, verbose_name='Telefone', validators=[validar_telefone])
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')
        
    def clean(self):
        # Remove máscara antes de validação
        self.telefone = re.sub(r'\D', '', self.telefone)
        self.cnpj = re.sub(r'\D', '', self.cnpj)

        # Verifica se o CNPJ já está cadastrado
        if CadastroFabricante.objects.filter(cnpj=self.cnpj).exclude(id=self.id).exists():
            raise ValidationError({'cnpj': "O CNPJ já foi cadastrado."})

    def save(self, *args, **kwargs):
        # Chama a validação antes de salvar
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'

    def __str__(self):
        return f"{self.id} - {self.nome}"
    
class CadastroTipoSensor(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    idOrigem = models.CharField(max_length=20, blank=True, null=True, verbose_name='Id de Origem')
    IdUnidadeMedida = models.ForeignKey(CadastroUnidadeMedida, on_delete=models.PROTECT, verbose_name='Unidade de Medida')
    leituraMinimaOperacao = models.FloatField(verbose_name='Leitura Mínima de Operação')
    leituraMaximaOperacao = models.FloatField(verbose_name='Leitura Máxima de Operação')
    leituraMinimaDesligado = models.FloatField(verbose_name='Leitura Mínima Desligado')
    leituraMaximaDesligado = models.FloatField(verbose_name='Leitura Máxima Desligado')
    leituraMinimaAlerta = models.FloatField(verbose_name='Leitura Mínima de Alerta')
    leituraMaximaAlerta = models.FloatField(verbose_name='Leitura Máxima de Alerta')
    leituraMinimaInterromper = models.FloatField(verbose_name='Leitura Mínima Interromper')
    leituraMaximaInterromper = models.FloatField(verbose_name='Leitura Máxima Interromper')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tipo de Sensor'
        verbose_name_plural = 'Tipos de Sensores'

    def __str__(self):
        return f"{self.id} - {self.descricao}"

class CadastroSensor(models.Model):
    descricao = models.CharField(max_length=200,verbose_name='Descrição')
    idOrigem = models.CharField(max_length=20, blank=True, null=True, verbose_name='Id de Origem')
    IdFabricante = models.ForeignKey(CadastroFabricante, on_delete=models.PROTECT, verbose_name='Fabricante')
    IdTipoSensor = models.ForeignKey(CadastroTipoSensor, on_delete=models.PROTECT, verbose_name='Tipo de Sensor')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'

    def __str__(self):
        return f"{self.id} - {self.descricao}"

class CadastroEquipamento(models.Model):
    descricao = models.CharField(max_length=200,verbose_name='Descrição')
    idOrigem = models.CharField(max_length=20, blank=True, null=True, verbose_name='Id de Origem')
    idFabricante = models.ForeignKey(CadastroFabricante, on_delete=models.PROTECT, verbose_name='Fabricante')
    descricaoInstalacao = models.TextField(verbose_name='Descrição de Instalação')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
    
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class InstalacaoSensor(models.Model):
    idSensor = models.ForeignKey(CadastroSensor, on_delete=models.PROTECT, verbose_name='Sensor')
    idEquipamento = models.ForeignKey(CadastroEquipamento, on_delete=models.PROTECT, verbose_name="Id do Equipamento")
    dataInstalacaoSensor = models.DateField(verbose_name='Data de instalação')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Atualizado em')
    data_remocao_sensor = models.DateField(blank=True, null=True, verbose_name='Data de Remoção')

    class Meta:
        verbose_name = 'Instalação de Sensor'
        verbose_name_plural = 'Instalação de Sensores'

    ##antes de salvar , preciso verificar se já existe alguma instalação com o id do sensor.    
    def clean(self):
        # Verificar se é um novo registro (não está sendo editado)
        if not self.pk:
            # Verificar se já existe uma instalação para o sensor sem data de remoção
            if InstalacaoSensor.objects.filter(idSensor=self.idSensor, data_remocao_sensor__isnull=True).exists():
                raise ValidationError(f"O sensor {self.idSensor} não pode ser instalado novamente sem a data de remoção preenchida.")
        
        # Certificar-se de que o idSensor está presente antes de salvar
        if not self.idSensor:
            raise ValidationError("O campo 'Sensor' não pode ser vazio.")
        
        super().clean()

    def __str__(self):
        return str(self.idSensor)

class CadastroLeitura(models.Model):
    idSensor = models.ForeignKey(CadastroSensor, on_delete=models.PROTECT, verbose_name='Sensor')
    idEquipamento = models.ForeignKey(CadastroEquipamento, on_delete=models.PROTECT, verbose_name="Equipamento")
    dataLeitura = models.DateTimeField(verbose_name='Data da Leitura')
    leitura = models.FloatField(verbose_name='Leitura')

    class Meta:
        verbose_name = 'Leitura'
        verbose_name_plural = 'Leituras'
    
    def clean(self):
        # Verificar se o sensor está instalado no equipamento informado
        if not InstalacaoSensor.objects.filter(idSensor=self.idSensor, idEquipamento=self.idEquipamento, data_remocao_sensor__isnull=True).exists():
            raise ValidationError(f"O sensor {self.idSensor} não está instalado no equipamento {self.idEquipamento}.")
        
        super().clean()
        

    def __str__(self):
        return str(self.idSensor)