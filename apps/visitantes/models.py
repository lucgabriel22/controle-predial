from django.db import models

class Visitantes(models.Model):

    STATUS_VISITANTE = [
        ('AGUARDANDO', 'Aguardando Autorização'),
        ('EM_VISITA', 'Em visita'),
        ('FINALIZADO', 'Visita Finalizada'),
    ]

    status = models.CharField(
        verbose_name='Status',
        max_length = 10,
        choices = STATUS_VISITANTE,
        default = 'AGUARDANDO',
    )

    nome_completo = models.CharField(
        verbose_name = 'Nome Completo',
        max_length = 100
    )

    cpf = models.CharField(
        verbose_name = 'CPF do Visitante',
        max_length = 11
    )

    data_nascimento = models.DateField(
        verbose_name = 'Data de Nascimento do Visitante',
        auto_now = False,
        auto_now_add = False
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name = 'Número da casa a ser visitada',
    )

    placa_veiculo = models.CharField(
        verbose_name = 'Placa do Veículo',
        max_length = 7,
        blank= True,
        null = True
    )

    horario_chegada = models.DateTimeField(
        verbose_name = 'Horário de chegada na portaria',
        auto_now_add = True

    )

    horario_saida = models.DateTimeField(
        verbose_name = 'Horário de saida do condomínio',
        auto_now_add = False,
        blank=True,
        null=True,

    )

    horario_autorizacao = models.DateTimeField(
        verbose_name = 'Horário de Autorização da Entrada',
        auto_now = False,
        blank = True,
        null = True,
    )

    morador_responsavel = models.CharField(
        verbose_name = 'Morador que autorizou a Entrada do visitante',
        max_length = 100,
        blank = True
    )

    registrado_por = models.ForeignKey(
        'porteiros.Porteiro',
        verbose_name = 'Porteiro responsável pelo registro',
        on_delete = models.PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return 'Horário de saída não registrado'
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
        return 'Visitante aguardando autorização'
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
        return 'Visitante aguardando autorização'
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
    
        return 'Veículo não registrado'
    
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_part_um = cpf[0:3]
            cpf_part_dois = cpf[3:6]
            cpf_part_tres = cpf[6:9]
            cpf_part_quatro = cpf[9:]

            cpf_formatado = f'{cpf_part_um}.{cpf_part_dois}.{cpf_part_tres}-{cpf_part_quatro}'

            return cpf_formatado
    


    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'

    def __str__(self):
        return self.nome_completo