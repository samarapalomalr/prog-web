from django.contrib import admin

from .models import Categoria, Mensagem                          # ALTERADO: importa Categoria


@admin.register(Categoria)                                       # NOVO
class CategoriaAdmin(admin.ModelAdmin):                          # NOVO
    list_display = ("nome",)                                     # NOVO
    search_fields = ("nome",)                                    # NOVO


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "criada_em")  # ALTERADO: + autor e categoria
    list_filter = ("categoria",)                                 # NOVO: filtro lateral por categoria
    search_fields = ("titulo", "conteudo")