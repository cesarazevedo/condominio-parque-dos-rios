from django.contrib import admin
from django.utils.html import format_html
from .models import Morador, Despesa, Taxa

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apartamento', 'bloco', 'telefone', 'ativo')
    list_filter = ('bloco', 'ativo')
    search_fields = ('nome', 'apartamento')

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria', 'valor', 'data')
    list_filter = ('categoria', 'data')
    search_fields = ('descricao',)
    date_hierarchy = 'data'

def marcar_como_pago(modeladmin, request, queryset):
    from django.utils import timezone
    queryset.update(status='pago', data_pagamento=timezone.now().date())

marcar_como_pago.short_description = "✅ Marcar selecionadas como PAGAS"

def marcar_como_atrasado(modeladmin, request, queryset):
    queryset.update(status='atrasado')

marcar_como_atrasado.short_description = "⚠️ Marcar selecionadas como ATRASADAS"

@admin.register(Taxa)
class TaxaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'descricao', 'valor', 'data_vencimento', 'status_colorido', 'data_pagamento')
    list_filter = ('status', 'data_vencimento')
    search_fields = ('morador__nome', 'descricao')
    date_hierarchy = 'data_vencimento'
    actions = [marcar_como_pago, marcar_como_atrasado]

    def status_colorido(self, obj):
        cores = {
            'pago': 'green',
            'pendente': 'orange',
            'atrasado': 'red',
        }
        cor = cores.get(obj.status, 'black')
        return format_html(
            '<strong style="color: {};">{}</strong>',
            cor,
            obj.get_status_display()
        )
    status_colorido.short_description = 'Status'