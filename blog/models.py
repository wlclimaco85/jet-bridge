from django.db import models
from django.urls import reverse

from users.models import MyUser

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})


class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class Xmls(models.Model):
    nomeFile = models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=255)
    xml = models.CharField(max_length=20000)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nomeFile

class StatusMaquinas(models.Model):
    nomeMaquina = models.CharField(max_length=255)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    dtUltVezOnLine = models.DateTimeField()

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nomeMaquina

class Corretora(models.Model):
    nome = models.CharField(max_length=100,blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True )
    senha = models.CharField(max_length=100, blank=True, null=True)
    aplicativo = models.CharField(max_length=50, blank=True, null=True, default='MetaTrader')
    server = models.CharField(max_length=50, blank=True, null=True, default='')
    empresa = models.CharField(max_length=50, blank=True, null=True, default='')
    ambiente = models.CharField(max_length=1, blank=True, null=True, default='D')
    moeda = models.CharField(max_length=10, blank=True, null=True, default='BRL')
    saldo = models.FloatField(blank=True, null=True, default=0)
    roboEnvioOrdem = models.CharField(max_length=1, blank=True, null=True, default='F')
    roboRecebimentoOrdem = models.CharField(max_length=1, blank=True, null=True, default='F')
    roboUpdateOrdem = models.CharField(max_length=1, blank=True, null=True, default='F')
    capitalLig = models.FloatField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class OrderEnvio(models.Model):
    simbolo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True, default=0)
    periodo = models.IntegerField(blank=True, null=True, default=0)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True, default='X')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE, blank=True, null=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo

class Estrategias(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True, default='')
    status = models.CharField(max_length=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    isteste = models.CharField(max_length=1, blank=True, null=True, default='N')
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class RequicaoEst(models.Model):
    estr_id = models.ForeignKey(Estrategias, on_delete=models.CASCADE)
    ordem_id = models.ForeignKey(OrderEnvio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.estr_id

class OrdemStatus(models.Model):
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE)
    ordem_id = models.ForeignKey(OrderEnvio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, blank=True, null=True, default='')
    motivo = models.CharField(max_length=200, blank=True, null=True, default='')
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class OrderCompraVenda(models.Model):
    ticket = models.IntegerField(blank=True, null=True)
    ordem_id = models.ForeignKey(OrderEnvio, on_delete=models.CASCADE, blank=True, null=True)
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE, blank=True, null=True)
    simbolo = models.CharField(max_length=255, blank=True, null=True, default='')
    ambiente = models.CharField(max_length=1, blank=True, null=True, default='D')
    nomeRobo = models.CharField(max_length=20, blank=True, null=True, default='RPBO0012')
    preco_compra = models.FloatField(blank=True, null=True, default=0)
    preco_venda = models.FloatField(blank=True, null=True, default=0)
    preco_loss = models.FloatField(blank=True, null=True, default=0)
    preco_gain = models.FloatField(blank=True, null=True, default=0)
    qtdContratos = models.IntegerField(blank=True, null=True, default=0)
    data_compra = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_venda = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True, default='X')
    perfil = models.CharField(max_length=1, blank=True, null=True, default='C')
    tipo = models.CharField(max_length=1, blank=True, null=True , default='X')
    positionId = models.IntegerField(blank=True, null=True, default=0)
    lucro = models.FloatField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo


class CustonResponse001(models.Model):
    corretora_id = models.IntegerField(db_column=False)
    ordem_id = models.IntegerField(db_column=False)
    tipo = models.CharField(max_length=1,db_column=False)
    status = models.CharField(max_length=1,db_column=False)
    simbolo = models.CharField(max_length=12,db_column=False)
    corretora = models.CharField(max_length=100,db_column=False)
    preco_compra  = models.FloatField(blank=True, null=True, db_column=False)
    preco_venda = models.FloatField(max_length=1,db_column=False)
    data_compra  = models.DateTimeField(blank=True, null=True, db_column=False)
    data_venda = models.DateTimeField(auto_now_add=True, db_column=False)
    created = models.DateTimeField(auto_now_add=True, db_column=False)
    ticket = models.IntegerField(db_column=False)
    preco_loss = models.FloatField(blank=True, null=True, db_column=False)
    preco_gain = models.FloatField(blank=True, null=True, db_column=False)
    class meta:
        ordering = ("-ordem_id",)
    def __str__(self):
        return self.id

class CustonResponse002(models.Model):
    id = models.IntegerField(primary_key=True, db_column=False)
    simbolo = models.CharField(blank=True, null=True, max_length=10,db_column=False)
    valor = models.FloatField(blank=True, null=True, db_column=False)
    periodo = models.IntegerField(blank=True, null=True, db_column=False)
    data = models.DateTimeField(blank=True, null=True, db_column=False)
    tipo = models.CharField(blank=True, null=True, max_length=1,db_column=False)
    created = models.DateTimeField(blank=True, null=True, db_column=False)
    updated = models.DateTimeField(blank=True, null=True, db_column=False)
    nome = models.CharField(blank=True, null=True, max_length=100,db_column=False)
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo


class CustonResponse004(models.Model):
    id = models.IntegerField(primary_key=True, db_column=False)
    simbolo = models.CharField(blank=True, null=True, max_length=10,db_column=False)
    valor = models.FloatField(blank=True, null=True, db_column=False)
    periodo = models.IntegerField(blank=True, null=True, db_column=False)
    data = models.DateTimeField(blank=True, null=True, db_column=False)
    tipo = models.CharField(blank=True, null=True, max_length=1,db_column=False)
    estr_id_id = models.IntegerField(blank=True, null=True, db_column=False)
    created = models.DateTimeField(blank=True, null=True, db_column=False)
    updated = models.DateTimeField(blank=True, null=True, db_column=False)
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo

class CustonResponse005(models.Model):
    id = models.IntegerField(primary_key=True, db_column=False)
    usuario = models.IntegerField(blank=True, null=True, db_column=False)
    ordem_abertas_hoje = models.IntegerField(blank=True, null=True, db_column=False)
    ordem_abertas_total = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_started = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_placed = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_canceled = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_partial = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_filled = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_rejected = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_expired = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_request_add = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_request_modify = models.IntegerField(blank=True, null=True, db_column=False)
    order_state_request_cancel = models.IntegerField(blank=True, null=True, db_column=False)
    ordem_erro = models.IntegerField(blank=True, null=True, db_column=False)
    ROBOENVIOORDEM = models.CharField(blank=True, null=True, db_column=False, max_length=1)
    ROBORECEBIMENTOORDEM = models.CharField(blank=True, null=True, db_column=False, max_length=1)
    ROBOUPDATEORDEM = models.CharField(blank=True, null=True, db_column=False, max_length=1)
    ordem_dia = models.IntegerField(blank=True, null=True, db_column=False)
    lucro = models.FloatField(blank=True, null=True, db_column=False)
    lucro1 = models.FloatField(blank=True, null=True, db_column=False)
    lucro2 = models.FloatField(blank=True, null=True, db_column=False)
    lucro3 = models.FloatField(blank=True, null=True, db_column=False)
    class meta:
        ordering = ("-ordem_erro",)
    def __str__(self):
        return self.ordem_erro

class CustonResponse006(models.Model):
    ordem_id_id = models.IntegerField(db_column=False)
    nome = models.CharField(blank=True, null=True,max_length=200, db_column=False)
    descricao = models.CharField(blank=True, null=True,max_length=200, db_column=False)
    class meta:
        ordering = ("-ordem_id_id",)
    def __str__(self):
        return self.ordem_id_id

class CustonResponse007(models.Model):
    id = models.IntegerField(primary_key=True, db_column=False)
    corretora_id = models.IntegerField(blank=True, null=True, db_column=False)
    ticket = models.IntegerField(blank=True, null=True, db_column=False)
    simbolo = models.CharField(max_length=200,blank=True, null=True, db_column=False)
    qtdContratos = models.IntegerField(blank=True, null=True, db_column=False)
    ordem_id_id = models.IntegerField(blank=True, null=True, db_column=False)
    positionId = models.IntegerField(blank=True, null=True, db_column=False)
    status = models.CharField(max_length=200,blank=True, null=True, db_column=False)
    tipo = models.CharField(max_length=200,blank=True, null=True, db_column=False)
    class meta:
        ordering = ("-ordem_id_id",)
    def __str__(self):
        return self.ordem_id_id

class OrdemZerada(models.Model):
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE)
    ordem_id = models.ForeignKey(OrderEnvio, on_delete=models.CASCADE)
    simbolo = models.CharField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, blank=True, null=True, default='Z')
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class Robos(models.Model):
    nome = models.CharField(max_length=100,blank=True, null=True)
    descricao = models.CharField(max_length=200,blank=True, null=True)
    dataUltUp = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    version = models.CharField(max_length=10,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True, default='Z')
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class Configuracoes(models.Model):
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE, blank=True, null=True)
    robo_id = models.ForeignKey(Robos, on_delete=models.CASCADE, blank=True, null=True)
    urlPrincipal = models.CharField(max_length=255, blank=True, null=True)
    dataConf = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    loteWin = models.FloatField(blank=True, null=True, default=0)
    loteWdo = models.FloatField(blank=True, null=True, default=0)
    loteB3 = models.FloatField(max_length=1, blank=True, null=True, default=0)
    gainDiario = models.FloatField(blank=True, null=True, default=0)
    lossDiario = models.FloatField(blank=True, null=True, default=0)
    seguranca = models.FloatField(blank=True, null=True, default=0)
    segurancaWDO = models.FloatField(blank=True, null=True, default=0)
    lossWin = models.FloatField(blank=True, null=True, default=0)
    gainWin = models.FloatField(blank=True, null=True, default=0)
    lossWdo = models.FloatField(blank=True, null=True, default=0)
    gainWdo = models.FloatField(blank=True, null=True, default=0)
    lossB3 = models.FloatField(blank=True, null=True, default=0)
    gainB3 = models.FloatField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class ConfiguracoesPorEst(models.Model):
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE, blank=True, null=True)
    estr_id = models.ForeignKey(Estrategias, on_delete=models.CASCADE)
    ativo = models.CharField(max_length=200,blank=True, null=True)
    dataConf = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lote = models.FloatField(blank=True, null=True, default=0)
    gainDiario = models.FloatField(blank=True, null=True, default=0)
    lossDiario = models.FloatField(blank=True, null=True, default=0)
    seguranca = models.FloatField(blank=True, null=True, default=0)
    loss = models.FloatField(blank=True, null=True, default=0)
    gain = models.FloatField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class CustonResponse008(models.Model):
    id = models.IntegerField(primary_key=True, db_column=False)
    corretora_id_id = models.IntegerField(blank=True, null=True, db_column=False)
    robo_id_id = models.IntegerField(blank=True, null=True, db_column=False)
    urlPrincipal = models.CharField(max_length=255, blank=True, null=True, db_column=False)
    dataConf = models.DateTimeField(auto_now_add=True, blank=True, null=True, db_column=False)
    loteWin = models.FloatField(blank=True, null=True, default=0, db_column=False)
    loteWdo = models.FloatField(blank=True, null=True, default=0, db_column=False)
    loteB3 = models.FloatField(max_length=1, blank=True, null=True, default=0, db_column=False)
    gainDiario = models.FloatField(blank=True, null=True, default=0, db_column=False)
    lossDiario = models.FloatField(blank=True, null=True, default=0, db_column=False)
    lossWin = models.FloatField(blank=True, null=True, default=0, db_column=False)
    gainWin = models.FloatField(blank=True, null=True, default=0, db_column=False)
    lossWdo = models.FloatField(blank=True, null=True, default=0, db_column=False)
    gainWdo = models.FloatField(blank=True, null=True, default=0, db_column=False)
    lossB3 = models.FloatField(blank=True, null=True, default=0, db_column=False)
    gainB3 = models.FloatField(blank=True, null=True, default=0, db_column=False)
    seguranca = models.FloatField(blank=True, null=True, default=0, db_column=False)
    segurancaWDO = models.FloatField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True, db_column=False)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True, db_column=False)
    class meta:
        ordering = ("-corretora_id_id",)
    def __str__(self):
        return self.corretora_id_id
    