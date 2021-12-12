from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ("nome", "cnpj", "author","status", "created", "updated")
    prepopulated_fields = {"cnpj": ("nome",)}

@admin.register(Xmls)
class XmlsAdmin(admin.ModelAdmin):
    list_display = ("nomeFile", "cnpj", "xml", "author","status", "created", "updated")
    prepopulated_fields = {"cnpj": ("nomeFile",)}

@admin.register(StatusMaquinas)
class StatusMaquinasAdmin(admin.ModelAdmin):
    list_display = ("nomeMaquina", "status", "author", "dtUltVezOnLine")
    prepopulated_fields = {"nomeMaquina": ("dtUltVezOnLine",)}

@admin.register(OrderEnvio)
class OrderEnvioAdmin(admin.ModelAdmin):
    list_display = ("simbolo", "valor", "status", "data", "tipo", "created", "updated")
    prepopulated_fields = {"simbolo": ("data",)}
