from django.db import models
from django.urls import reverse_lazy

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NMC', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=11, decimal_places=2)
    estoque = models.IntegerField('Estoque_atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)
    categoria = models.ForeignKey(
            'Categoria',
            on_delete=models.SET_NULL,
            null=True,
            blank=True
            )

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk':self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }


class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_list')

    def __str__(self):
        return self.categoria
