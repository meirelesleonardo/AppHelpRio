from operator import mod
from django.db import models
from django.urls import clear_url_caches
from apps.instituicao.models import Instituicao
from users.models import User


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

class Proprietario(models.Model):
    ProprietarioId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000, blank=True, null=True)
    TelCelular = models.CharField(max_length=100, blank=True, null=True)
    TelResidencial = models.CharField(max_length=500, blank=True, null=True)
    TelComercial = models.CharField(max_length=500, blank=True, null=True)
    E_mail = models.CharField(max_length=500, blank=True, null=True)
    Conjge = models.CharField(max_length=500, blank=True, null=True)
    ConjugeCel = models.CharField(max_length=500, blank=True, null=True)
    ConjugeE_mail = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nome

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

    SIM_NAO = (
        (0,'Sim'),
        (1, 'Nao'),        
    )

    FichaImovelId = models.AutoField(primary_key=True)
    CodigoUnico = models.CharField(max_length=100, blank=True, null=True)
    DataCadastro = models.DateTimeField(auto_now_add=True)
    CantoDePedra = models.BooleanField(default=False)
    MotivoCantoDePedra = models.CharField(max_length=300, blank=True, null=True)

    Posicao = models.IntegerField(choices=POSICAO, default=0)
    Sol = models.CharField(max_length=1, choices=SOL, blank=True, null=True)
    SituacaoImovel = models.IntegerField(choices=SITUACAO_IMOVEL, blank=True, null=True)

    Placa = models.CharField(max_length=100, blank=True, null=True)
    Chave = models.CharField(max_length=100, blank=True, null=True)

    Quartos = models.IntegerField(blank=True, null=True)
    Suites = models.IntegerField(blank=True, null=True)
    Banheiros = models.IntegerField(blank=True, null=True)
    Vagas = models.IntegerField(blank=True, null=True)
    Subsolo = models.IntegerField(choices=SIM_NAO, default=1)
    ElevadorSocial = models.BooleanField(default=True)
    ElevadorServico = models.BooleanField(default=True)
    NumeroPavmento = models.IntegerField(blank=True, null=True)
    UnidadeAndar = models.IntegerField(blank=True, null=True)
    Idade = models.IntegerField(blank=True, null=True)

    AreaTerreno = models.FloatField(blank=True, null=True)
    AreaConstruida = models.FloatField(blank=True, null=True)
    ValorCondominio = models.FloatField(blank=True, null=True)
    HidrometroIndvidual = models.IntegerField(choices=SIM_NAO, default=0)
    IptuAtual = models.FloatField(blank=True, null=True)
    NumeroInscricao = models.IntegerField(blank=True, null=True)

    ValorVenda = models.FloatField(blank=True, null=True)
    EntregaEm = models.DateField(blank=True, null=True)
    AceitaPermuta = models.IntegerField(choices=SIM_NAO, default=1)
    Aonde = models.CharField(max_length=1000, blank=True, null=True)
    MotivoDavenda = models.CharField(max_length=1000, blank=True, null=True)

    OnibusVan = models.IntegerField(choices=SIM_NAO, default=1)
    balsa = models.IntegerField(choices=SIM_NAO, default=1)
    Dependencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    FotosImovel = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    FotosCondominio = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    PlayGround = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    Piscina = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    Academia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    AreaGourmet = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    Sauna = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    SalaoDeFestas = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    QuadraSports = models.IntegerField(choices=SIM_NAO, blank=True, null=True)

    Opcionista =  models.CharField(max_length=100, blank=True, null=True)
    Comissao = models.FloatField(blank=True, null=True)
    CaptacaoFicha = models.FloatField(blank=True, null=True) 
    outro = models.CharField(max_length=1000, blank=True, null=True)
    HabiteSe = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    DocumentacaoNaEmpresa = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    qual =  models.CharField(max_length=500, blank=True, null=True)
    Descricao = models.TextField(max_length=20000, blank=True, null=True)

    DataAtualizacao = models.DateTimeField(auto_now=True)
    AtualizacaoObs = models.CharField(max_length=20000, blank=True, null=True)
    
    Proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, blank=True, null=True)
    DataUltimaModificacao = models.DateTimeField(auto_now=True)
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    Condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, null=True, blank=True)
    CondicoesObs = models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.CodigoUnico

