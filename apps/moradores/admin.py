from django.contrib import admin
from .models import Moradores


@admin.register(Moradores)
class MoradoresAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'numero_casa', 'placa_veiculo', 'foto_morador')
    list_display_links = ('nome_completo', 'cpf')
    search_fields = ('nome_completo', 'cpf', 'data_nascimento', 'numero_casa', 'placa_veiculo', 'foto_morador')
    list_per_page = 5
    ordering = ['-numero_casa']
