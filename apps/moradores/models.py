from django.db import models

class Moradores(models.Model):
    nome_completo = models.CharField(
        max_length=100,
        blank=False

    )
    cpf = models.CharField(
        max_length=11,
        blank=False
    )
    data_nascimento = models.DateField()

    numero_casa = models.IntegerField(
        blank=False
    )

    placa_veiculo = models.CharField(
        max_length=7,
        blank=True
    )
    

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_part_um = cpf[0:3]
            cpf_part_dois = cpf[3:6]
            cpf_part_tres = cpf[6:9]
            cpf_part_quatro = cpf[9:]

            cpf_formatado = f'{cpf_part_um}.{cpf_part_dois}.{cpf_part_tres}-{cpf_part_quatro}'

            return cpf_formatado

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'
        db_table = 'morador'
       



