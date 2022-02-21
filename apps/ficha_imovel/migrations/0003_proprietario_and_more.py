# Generated by Django 4.0.1 on 2022-02-20 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_imovel', '0002_fichaimovel_academia_fichaimovel_aceitapermuta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('ProprietarioId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=1000, null=True)),
                ('TelCelular', models.CharField(blank=True, max_length=100, null=True)),
                ('TelResidencial', models.CharField(blank=True, max_length=500, null=True)),
                ('TelComercial', models.CharField(blank=True, max_length=500, null=True)),
                ('E_mail', models.CharField(blank=True, max_length=500, null=True)),
                ('Conjge', models.CharField(blank=True, max_length=500, null=True)),
                ('ConjugeCel', models.CharField(blank=True, max_length=500, null=True)),
                ('ConjugeE_mail', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='fichaimovel',
            old_name='CondominioFk',
            new_name='Condominio',
        ),
        migrations.RenameField(
            model_name='fichaimovel',
            old_name='InstituicaoFk',
            new_name='Instituicao',
        ),
        migrations.AddField(
            model_name='fichaimovel',
            name='Proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ficha_imovel.proprietario'),
        ),
    ]
