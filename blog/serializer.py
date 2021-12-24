from  rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','slug','author','body']

class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiro
        fields = ['id','nome','cnpj','author','status','created','updated']

class StatusMaquinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMaquinas
        fields = ['id','nomeMaquina','status','author','dtUltVezOnLine']

class XmlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xmls
        fields = ['id','nomeFile','cnpj','author','xml','status','created','updated']

class OrderEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderEnvio
        fields = ['id','simbolo','valor','data','tipo','periodo','created','updated']

class CorretoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corretora
        fields = ['id','nome','usuario','senha','aplicativo','ambiente','saldo','created','updated','server','empresa','moeda','saldo','capitalLig']

class EstrategiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrategias
        fields = ['id','nome','descricao','status','created','updated']

class RequicaoEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequicaoEst
        fields = ['id','estr_id','ordem_id','created','updated']

class OrdemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemStatus
        fields = ['id','corretora_id','ordem_id','status', 'created','updated']

class OrderCompraVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCompraVenda
        fields = ['id','corretora_id','ticket','ordem_id','simbolo','ambiente','nomeRobo','corretora','preco_compra','preco_venda','preco_loss','preco_gain','qtdContratos','data_compra','data_venda','status','tipo','created','updated']

class CustonResponse001Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse001
        fields = ['corretora_id','ordem_id','status','corretora','tipo','simbolo','preco_compra','preco_venda','data_compra','data_venda','created','ticket','preco_loss','preco_gain']

class CustonResponse002Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse002
        fields = ['id','simbolo','valor','periodo','data','tipo','created','updated','nome']


