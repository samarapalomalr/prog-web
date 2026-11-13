from django.contrib import admin

from .models import Categoria, Mensagem, Tag                     # ALTERADO: importa Tag


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Tag)                                             # NOVO
class TagAdmin(admin.ModelAdmin):                                # NOVO
    list_display = ("nome",)                                     # NOVO
    search_fields = ("nome",)                                    # NOVO


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "criada_em")
    list_filter = ("categoria", "tags")                          # ALTERADO: + filtro por tags
    search_fields = ("titulo", "conteudo")
    filter_horizontal = ("tags",)                                # NOVO: seletor de dois painéis para tags