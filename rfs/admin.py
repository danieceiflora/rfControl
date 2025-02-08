from django.contrib import admin
from .models import CadastroUnidadeMedida, CadastroFabricante, CadastroSensor, CadastroEquipamento, CadastroTipoSensor, InstalacaoSensor
from django.db.models import Q
from django.db.models import OuterRef



class unidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('id','descricao', 'idOrigem', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroUnidadeMedida, unidadeMedidaAdmin)

class CadastroFabricanteAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin_custom.js',)

    list_display = ('id', 'nome',  'cnpj_formatado', 'telefone_formatado', )
    search_fields = ('nome', 'id')
    

    def telefone_formatado(self, obj):
        telefone = obj.telefone
        if len(telefone) == 11:
            return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    telefone_formatado.short_description = 'Telefone'

    def cnpj_formatado(self, obj):
        return f"{obj.cnpj[:2]}.{obj.cnpj[2:5]}.{obj.cnpj[5:8]}/{obj.cnpj[8:12]}-{obj.cnpj[12:]}"
    cnpj_formatado.short_description = 'CNPJ'

admin.site.register(CadastroFabricante, CadastroFabricanteAdmin)

class CadastroSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'IdFabricante', 'IdTipoSensor', 'is_available', 'listar_equipamentos')
    search_fields = ('descricao', 'id')
    #retornar um listdisplay com um campo para mostrar se está disponível ou não, para verificar isto
    #preciso verificar se o sensor existe na tabela de instalação, se existir, mas estiver com data de remoção, entao ele nao esta disponivel
    #se não existir, também está disponível
    def is_available(self, obj):
        latest_installation = InstalacaoSensor.objects.filter(idSensor=obj).order_by('-dataInstalacaoSensor').first()
        if latest_installation and (latest_installation.data_remocao_sensor is None or latest_installation.dataInstalacaoSensor > latest_installation.data_remocao_sensor):
            return "Indisponível"
        return "Disponível"
    is_available.short_description = 'Status'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['IdFabricante', 'IdTipoSensor']
        return []

    ## vamos criar um list_display para mostrar os sensores instalados em um equipamento, eu quero retornar o equipamento em que ele está instalado.
    def listar_equipamentos(self, obj):
        equipamentos = []
        for sensor in obj.instalacaosensor_set.all():
            if sensor.data_remocao_sensor is None or sensor.dataInstalacaoSensor > sensor.data_remocao_sensor:
                equipamentos.append(sensor.idEquipamento.descricao)
        return ", ".join(equipamentos) if equipamentos else "Nenhum equipamento instalado"
    listar_equipamentos.short_description = 'Equipamentos Instalados'
    fieldsets = (
        ('Informaçõe do Sensor', {
            'fields': ( 'IdTipoSensor', 'IdFabricante', 'descricao',)
        }),

    )

admin.site.register(CadastroSensor, CadastroSensorAdmin)

class SensoresInstaladosInline(admin.TabularInline):
    model = InstalacaoSensor
    fields = ('idSensor', 'dataInstalacaoSensor', 'data_remocao_sensor')
    readonly_fields = ('idSensor', 'dataInstalacaoSensor')
    can_delete = False
    extra = 0
    verbose_name = 'Sensor Instalado'
    verbose_name_plural = 'Sensores Instalados'
    
    ## retornar apenas os sensores que não tem data de remoção preenchidos
    def get_queryset(self, request):
        # Retorna apenas os sensores que não tem data de remoção preenchidos
        return super().get_queryset(request).filter(data_remocao_sensor__isnull=True)

    def has_add_permission(self, request, obj=None):
        return False  # Não permite adicionar sensores aqui


class AdicionarSensorInline(admin.TabularInline):
    model = InstalacaoSensor
    fields = ('idSensor', 'dataInstalacaoSensor')
    extra = 1
    can_delete = False

    def get_queryset(self, request):
        # Retorna apenas os novos sensores a serem adicionados
        return super().get_queryset(request).none()


    ##mostrar apenas sensores não instalados para adicionar
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'idSensor':
            obj_id = request.resolver_match.kwargs.get('object_id')
            if obj_id:
                # Mostra apenas sensores não instalados ou removidos
                kwargs['queryset'] = CadastroSensor.objects.filter(
                    Q(instalacaosensor__isnull=True) |
                    (Q(instalacaosensor__data_remocao_sensor__isnull=False) &
                     ~Q(instalacaosensor__dataInstalacaoSensor__lt=InstalacaoSensor.objects.filter(idSensor=OuterRef('id'), data_remocao_sensor__isnull=True).order_by('-dataInstalacaoSensor').values('dataInstalacaoSensor')[:1]))
                ).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CadastroEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'idFabricante', 'listar_sensores', 'qtd_sensores')
    search_fields = ('descricao', 'id')
    inlines = [SensoresInstaladosInline, AdicionarSensorInline]


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['idFabricante',]
        return []

    fieldsets = (
        ('Informaçõe do Equipamento', {
            'fields': ('idFabricante', 'descricao', 'descricaoInstalacao')
        }),
  

    )

    ## listar apenas sensores com data de remoção em branco.
    def listar_sensores(self, obj):
        sensores = obj.instalacaosensor_set.filter(data_remocao_sensor__isnull=True).values_list('idSensor__descricao', flat=True)
        return ", ".join(sensores) if sensores else "Nenhum sensor instalado"

    listar_sensores.short_description = "Sensores Instalados"

    def qtd_sensores(self, obj):
        return obj.instalacaosensor_set.filter(data_remocao_sensor__isnull=True).count()

    qtd_sensores.short_description = "Quantidade de Sensores"

admin.site.register(CadastroEquipamento, CadastroEquipamentoAdmin)


class CadastroTipoSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao',  'IdUnidadeMedida',)
    search_fields = ('descricao', 'id' )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['IdUnidadeMedida',]
        return []
    
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('Informaçõe do Tipo de Sensor', {
                'fields': ( 'IdUnidadeMedida', 'descricao',)
            }),
            (
                'Informação de leitura', {
                    'fields': ('leituraMinimaOperacao', 'leituraMaximaOperacao', 'leituraMinimaDesligado', 'leituraMaximaDesligado', 'leituraMinimaAlerta', 'leituraMaximaAlerta', 'leituraMinimaInterromper', 'leituraMaximaInterromper')}
            ),
        )
        return fieldsets

    
admin.site.register(CadastroTipoSensor, CadastroTipoSensorAdmin)

class InstalacaoSensorAdmin(admin.ModelAdmin):

    list_display = ('id', 'idSensor',  'idEquipamento__id' , 'idEquipamento__descricao' , 'dataInstalacaoSensor', 'data_remocao_sensor') 
    search_fields = ('descricao', 'id')  

    def save_model(self, request, obj, form, change):       
        # Salvar o modelo
        super().save_model(request, obj, form, change)
    


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['idSensor', 'idEquipamento',]
        return []
    def get_fieldsets(self, request, obj =None):

        fieldsets = (
            ('Dados da Instalação', {
                'fields': ('idSensor', 'idEquipamento', 'dataInstalacaoSensor',)
            }),
            ('Remoção do Sensor', {
                'fields': ('data_remocao_sensor',)
            })
        
        )
        
        return fieldsets


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'idSensor':
                    # Filter sensors that are not installed or have been removed
                kwargs['queryset'] = CadastroSensor.objects.filter(
                    Q(instalacaosensor__isnull=True) |
                    (Q(instalacaosensor__data_remocao_sensor__isnull=False) &
                     ~Q(instalacaosensor__dataInstalacaoSensor__lt=InstalacaoSensor.objects.filter(idSensor=OuterRef('id'), data_remocao_sensor__isnull=True).order_by('-dataInstalacaoSensor').values('dataInstalacaoSensor')[:1]))
                ).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
      
admin.site.register(InstalacaoSensor, InstalacaoSensorAdmin)

