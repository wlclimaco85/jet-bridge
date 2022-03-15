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
    list_display = ('id','simbolo','valor','data','tipo', 'periodo', 'created','updated')

@admin.register(OrdemStatus)
class OrdemStatusAdmin(admin.ModelAdmin):
    list_display = ('id','corretora_id','ordem_id','status', 'created','updated')

@admin.register(Corretora)
class CorretoraAdmin(admin.ModelAdmin):
    list_display = ('id','nome','usuario','senha','aplicativo','ambiente','saldo','created','updated','server','empresa','moeda','saldo','capitalLig')

@admin.register(RequicaoEst)
class RequicaoEstAdmin(admin.ModelAdmin):
    list_display = ('id','estr_id','ordem_id','created','updated')

@admin.register(Estrategias)
class EstrategiasAdmin(admin.ModelAdmin):
    list_display = ('id','nome','descricao','status','created','updated')

@admin.register(OrderCompraVenda)
class OrderCompraVendaAdmin(admin.ModelAdmin):
    list_display = ('id','ticket','ordem_id','simbolo','ambiente','nomeRobo','preco_compra','preco_venda','preco_loss','preco_gain','qtdContratos','data_compra','data_venda','status','tipo','created','updated')

@admin.register(Robos)
class RobosAdmin(admin.ModelAdmin):
    list_display = ('id','nome','descricao','dataUltUp','version','created','updated','status')

@admin.register(Configuracoes)
class ConfiguracoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'corretora_id','robo_id','urlPrincipal','dataConf','loteWin','loteWdo','seguranca','segurancaWDO','loteB3','gainDiario','lossDiario','lossWin','gainWin','lossWdo','gainWdo','lossB3','gainB3','created','updated')
