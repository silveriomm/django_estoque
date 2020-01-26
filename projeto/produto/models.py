from django.db import models

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NMC', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=11, decimal_places=2)
    estoque = models.IntegerField('Estoque_atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto