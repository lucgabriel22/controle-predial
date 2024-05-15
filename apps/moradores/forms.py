from django import forms
from .models import Moradores


class MoradorForm(forms.ModelForm):
    class Meta:
        model = Moradores
        fields = [
            'nome_completo', 'cpf', 'data_nascimento', 'numero_casa', 'placa_veiculo', 'foto_morador'
        ]

        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Nome Completo'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'numero_casa': forms.TextInput(attrs={'placeholder': 'Numero da casa'}),
            'placa_veiculo': forms.TextInput(attrs={'placeholder': 'Placa do veiculo'}),
            
        }

        labels = {
            'nome_completo': 'Nome Completo',
            'cpf': 'CPF',
            'data_nascimento': 'Data de Nascimento',
            'numero_casa': 'Numero da casa',
            'placa_veiculo': 'Placa do veiculo',
            'foto_morador': 'Foto do morador',  
        }

        help_texts = {
            
        }
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

            'foto_morador': {
                'required': 'Por favor, insira uma foto do morador'
                
            }

        }


    