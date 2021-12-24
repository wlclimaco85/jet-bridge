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
    nome = models.CharField(max_length=100)
    usuario = models.IntegerField(blank=True, null=True )
    senha = models.CharField(max_length=100, blank=True, null=True)
    aplicativo = models.CharField(max_length=50, blank=True, null=True)
    server = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)
    ambiente = models.CharField(max_length=1, blank=True, null=True)
    moeda = models.CharField(max_length=10, blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    capitalLig = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class OrderEnvio(models.Model):
    simbolo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo

class Estrategias(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

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
    status = models.CharField(max_length=1, blank=True, null=True)
    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.id

class OrderCompraVenda(models.Model):
    ticket = models.IntegerField(blank=True, null=True)
    ordem_id = models.ForeignKey(OrderEnvio, on_delete=models.CASCADE, blank=True, null=True)
    corretora_id = models.ForeignKey(Corretora, on_delete=models.CASCADE, blank=True, null=True)
    simbolo = models.CharField(max_length=255, blank=True, null=True)
    ambiente = models.CharField(max_length=1, blank=True, null=True)
    nomeRobo = models.CharField(max_length=20, blank=True, null=True)
    preco_compra = models.FloatField(blank=True, null=True)
    preco_venda = models.FloatField(blank=True, null=True)
    preco_loss = models.FloatField(blank=True, null=True)
    preco_gain = models.FloatField(blank=True, null=True)
    qtdContratos = models.IntegerField(blank=True, null=True)
    data_compra = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_venda = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    perfil = models.CharField(max_length=1, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True )
    corretora = models.CharField(max_length=100, blank=True, null=True)
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


    

    