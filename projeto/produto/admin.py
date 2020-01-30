from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'categoria',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields = ('produto',)
    list_filter = ('importado',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    search_fields = ('categoria',)
