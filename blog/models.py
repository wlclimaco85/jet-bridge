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

class OrderEnvio(models.Model):
    simbolo = models.CharField(max_length=255)
    valor = models.FloatField()
    status = models.CharField(max_length=1)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.simbolo


    

    