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
        fields = ['id','simbolo','valor','status','data','tipo','created','updated']