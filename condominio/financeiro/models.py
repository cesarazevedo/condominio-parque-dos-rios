from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    apartamento = models.CharField(max_length=10)
    bloco = models.CharField(max_length=5)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    data_entrada = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - Apto {self.apartamento} Bloco {self.bloco}"
class Despesa(models.Model):
    CATEGORIAS = [
        ('agua', 'Água'),
        ('luz', 'Luz'),
        ('limpeza', 'Limpeza'),
        ('manutencao', 'Manutenção'),
        ('seguranca', 'Segurança'),
        ('outros', 'Outros'),
    ]

    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.data})"


class Taxa(models.Model):
    STATUS = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('atrasado', 'Atrasado'),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pendente')

    def __str__(self):
        return f"{self.morador.nome} - {self.descricao} - {self.status}"