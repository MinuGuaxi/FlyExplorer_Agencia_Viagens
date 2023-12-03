from django.db import models

class Hotel(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    servicos     = models.CharField(max_length=255)
    imagem       = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table='hotel'
    def _str__(self):
        return self.nome

class Passagem(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    servicos     = models.CharField(max_length=255)
    destinos     = models.CharField(max_length=255)

    class Meta:
        db_table='passagem'
    def _str__(self):
        return self.nome

class Pacotes(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    expedicao    = models.CharField(max_length=50)
    servicos     = models.CharField(max_length=255)
    descricao    = models.CharField(max_length=255)
    imagem       = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table='pacotes'
    def _str__(self):
        return self.nome


class Ofertas(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    tipo         = models.CharField(max_length=50)
    servicos     = models.CharField(max_length=255)
    descricao    = models.CharField(max_length=255)
    imagem       = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table='ofertas'
    def _str__(self):
        return self.nome


class Alugueis(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    tipo         = models.CharField(max_length=50)
    servicos     = models.CharField(max_length=255)
    descricao    = models.CharField(max_length=255)
    imagem       = models.ImageField(upload_to='static/img/')

    class Meta:
        db_table='alugueis'
    def _str__(self):
        return self.nome


class Seguros(models.Model):
    id           = models.CharField(primary_key=True, max_length=255)
    nome         = models.CharField(max_length=50)
    telefone     = models.CharField(max_length=50)
    valor        = models.CharField(max_length=50)
    tipo         = models.CharField(max_length=50)
    descricao    = models.CharField(max_length=255)

    class Meta:
        db_table='seguros'
    def _str__(self):
        return self.nome