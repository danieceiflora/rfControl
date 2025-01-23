from django.contrib import admin
from .models import CadastroUnidadeMedida, CadastroFabricante, CadastroSensor, CadastroEquipamento, CadastroTipoSensor, InstalacaoSensor
from django.db.models import Q


class unidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('id','descricao', 'idOrigem', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroUnidadeMedida, unidadeMedidaAdmin)

class CadastroFabricanteAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin_custom.js',)

    list_display = ('id', 'nome', 'idOrigem', 'cnpj_formatado', 'telefone_formatado', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'idOrigem')
    

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
    list_display = ('id', 'descricao', 'idOrigem', 'IdFabricante', 'IdTipoSensor', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroSensor, CadastroSensorAdmin)

class InstalacaoSensorInline(admin.TabularInline):
    model = InstalacaoSensor
    fields = ('idSensor',  'dataInstalacaoSensor')
    show_change_link = False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'idSensor':
            # Aplicar o filtro para sensores
            kwargs['queryset'] = CadastroSensor.objects.filter(
                Q(instalacaosensor__isnull=True) |  # Sensores sem instalação
                Q(instalacaosensor__data_remocao_sensor__isnull=False)  # Sensores com data de remoção
            ).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CadastroEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'idOrigem', 'idFabricante',  'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')
  
    inlines = [InstalacaoSensorInline]
    show_change_link = False

admin.site.register(CadastroEquipamento, CadastroEquipamentoAdmin)


class CadastroTipoSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'idOrigem', 'IdUnidadeMedida', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')
    
admin.site.register(CadastroTipoSensor, CadastroTipoSensorAdmin)

class InstalacaoSensorAdmin(admin.ModelAdmin):

    list_display = ('id', 'idSensor',  'idEquipamento__id' , 'idEquipamento__descricao', 'dataInstalacaoSensor', 'data_remocao_sensor','criado_em', 'atualizado_em') 
    search_fields = ('idSensor__descricao',)   

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'idSensor':
            if 'change' not in request.path:
                    # Filter sensors that are not installed or have been removed
                kwargs['queryset'] = CadastroSensor.objects.filter(
                    Q(instalacaosensor__isnull=True) |  # Sensors with no installation
                    Q(instalacaosensor__data_remocao_sensor__isnull=False)  # Sensors with removal date
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
      
admin.site.register(InstalacaoSensor, InstalacaoSensorAdmin)

