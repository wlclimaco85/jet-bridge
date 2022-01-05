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
        fields = ['id','nome','usuario','senha','aplicativo','ambiente','saldo','created','updated','server','empresa','moeda','saldo','capitalLig','roboEnvioOrdem','roboRecebimentoOrdem','roboUpdateOrdem']

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
        fields = ['id','corretora_id','ticket','ordem_id','simbolo','ambiente','nomeRobo','preco_compra','preco_venda','preco_loss','preco_gain','qtdContratos','data_compra','data_venda','status','tipo','created','updated']

class CustonResponse001Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse001
        fields = ['corretora_id','ordem_id','status','tipo','simbolo','preco_compra','preco_venda','data_compra','data_venda','created','ticket','preco_loss','preco_gain']

class CustonResponse002Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse002
        fields = ['id','simbolo','valor','periodo','data','tipo','created','updated','nome']

class CustonResponse004Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse004
        fields = ['id','simbolo','valor','periodo','data','tipo','created','updated']

class CustonResponse005Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse005
        fields = ['id','usuario','ordem_abertas_hoje','ordem_abertas_total','order_state_started' ,'order_state_placed' ,'order_state_canceled' ,'order_state_partial' , 'order_state_filled' ,'order_state_rejected' ,'order_state_expired' ,'order_state_request_add' ,'order_state_request_modify','order_state_request_cancel' ,'ordem_erro'  ]

class CustonResponse006Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustonResponse006
        fields = ['ordem_id_id','nome','descricao']