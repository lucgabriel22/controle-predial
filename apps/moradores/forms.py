from django import forms
from moradores.models import Moradores

class MoradorForm(forms.ModelForm):
    class Meta:
        model = Moradores
        fields = [
            'nome_completo', 'cpf', 'data_nascimento', 'numero_casa', 'placa_veiculo'
        ]

        error_messages = {
            'nome_completo': {
                'required': 'O nome completo do morador é obrigatório para o registro'
            },
        
            'cpf': {
                'required': 'O  CPF do morador é obrigatório para o registro'
                },
          
            'data_nascimento': {
                'required': 'A data de nascimento do morador é obrigatório para o registro',
                'invalid': 'Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)'
            },
            'numero_casa': {
                'required': 'Por favor, informe o número da casa'
                },

        }


        error_messages = {
            'morador_responsavel': {
                'required': 'Por favor, informe o nome do morador responsável por autorizar a entrada do visitante!'
            }
        }