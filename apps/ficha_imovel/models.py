from django.db import models
from apps.instituicao.models import Instituicao


class Condominio(models.Model):
    CondominioId = models.AutoField(primary_key=True)
    Condominio = models.CharField(max_length=1000, blank=True, null=True)
    Tipo = models.CharField(max_length=100, blank=True, null=True)
    Bairro = models.CharField(max_length=100, blank=True, null=True)
    Endereco = models.CharField(max_length=1000, blank=True, null=True)
    Localizacao = models.CharField(max_length=1000, blank=True, null=True)
    NomeDoEdificio = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.Condominio


class FichaImovel(models.Model):
    FichaImovelId = models.AutoField(primary_key=True)
    CodigoUnico = models.CharField(max_length=100, blank=True, null=True)
    DataCadastro = models.DateTimeField(auto_now_add=True)
    CantoDePedra = models.BooleanField(default=True)
    MotivoCantoDePedra = models.CharField(max_length=300, blank=True, null=True)

    
    DataUltimaModificacao = models.DateTimeField(auto_now=True)
    InstituicaoFk = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    CondominioFk = models.ForeignKey(Condominio, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.CodigoUnico

