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

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'
        db_table = 'morador'


