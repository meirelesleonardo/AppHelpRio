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
    POSICAO = (
        (0,''),
        (1,'Fundos'),
        (2, 'Frente'),
        (3, 'Lateral'),
    )

    SOL = (
        ('M','Manhã'),
        ('T', 'Tarde'),
    )

    SITUACAO_IMOVEL = (
        (0,'Vazio'),
        (1, 'Ocupado'),        
    )

    SUBSOLO = (
        (0,'Sim'),
        (1, 'Nao'),        
    )

    FichaImovelId = models.AutoField(primary_key=True)
    CodigoUnico = models.CharField(max_length=100, blank=True, null=True)
    DataCadastro = models.DateTimeField(auto_now_add=True)
    CantoDePedra = models.BooleanField(default=False)
    MotivoCantoDePedra = models.CharField(max_length=300, blank=True, null=True)

    Posicao = models.IntegerField(choices=POSICAO, default=0)
    Sol = models.CharField(max_length=1, choices=SOL)
    SituacaoImovel = models.IntegerChoices(choices=SITUACAO_IMOVEL)

    Placa = models.CharField(max_length=100, blank=True, null=True)
    Chave = models.CharField(max_length=100, blank=True, null=True)

    Quartos = models.IntegerField(blank=True, null=True)
    Suites = models.IntegerField(blank=True, null=True)
    Banheiros = models.IntegerField(blank=True, null=True)
    Vagas = models.IntegerField(blank=True, null=True)
    Subsolo = models.IntegerField(choices=SUBSOLO, default=1)
    ElevadorSocial = models.BooleanField(default=True)
    ElevadorServico = models.BooleanField(default=True)
    NumeroPavmento = models.IntegerField(blank=True, null=True)
    UnidadeAndar = models.IntegerField(blank=True, null=True)
    Idade = models.IntegerField(blank=True, null=True)
    
    DataUltimaModificacao = models.DateTimeField(auto_now=True)
    InstituicaoFk = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    CondominioFk = models.ForeignKey(Condominio, on_delete=models.CASCADE, null=True, blank=True)

    
    

    def __str__(self):
        return self.CodigoUnico

