from django.contrib import admin
from .models import CadastroUnidadeMedida, CadastroFabricante, CadastroSensor, CadastroEquipamento, CadastroTipoSensor



class unidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'idOrigem', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroUnidadeMedida, unidadeMedidaAdmin)

class CadastroFabricanteAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin_custom.js',)

    list_display = ('nome', 'idOrigem', 'cnpj_formatado', 'telefone_formatado', 'criado_em', 'atualizado_em')
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
    list_display = ('descricao', 'idOrigem', 'IdFabricante', 'IdTipoSensor', 'dataInstalacao', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroSensor, CadastroSensorAdmin)

class CadastroEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'idOrigem', 'idSensor__dataInstalacao', 'idFabricante',  'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroEquipamento, CadastroEquipamentoAdmin)

class CadastroTipoSensorAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'idOrigem', 'IdUnidadeMedida', 'criado_em', 'atualizado_em')
    search_fields = ('descricao', 'idOrigem')

admin.site.register(CadastroTipoSensor, CadastroTipoSensorAdmin)
