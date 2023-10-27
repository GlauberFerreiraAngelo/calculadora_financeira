from django.db import models

class Renda(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    # Adicione outros campos conforme necessário para a validação de renda

    def __str__(self):
        return f'Renda de {self.valor}'

class Emprestimo(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.PositiveIntegerField()
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2)
    # Adicione outros campos conforme necessário para o cálculo de empréstimo

    def __str__(self):
        return f'Empréstimo de {self.valor} a {self.taxa_juros}%'

