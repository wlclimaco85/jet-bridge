# Generated by Django 3.2.7 on 2021-12-13 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corretora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('aplicativo', models.CharField(max_length=50)),
                ('ambiente', models.CharField(max_length=1)),
                ('saldo', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estrategias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='orderenvio',
            name='ambiente',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RequicaoEst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('estr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.estrategias')),
                ('ordem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.orderenvio')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCompraVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=255)),
                ('ambiente', models.CharField(max_length=1)),
                ('nomeRobo', models.CharField(max_length=20)),
                ('preco_compra', models.FloatField()),
                ('preco_venda', models.FloatField()),
                ('preco_loss', models.FloatField()),
                ('preco_gain', models.FloatField()),
                ('qtdContratos', models.IntegerField()),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('data_venda', models.DateTimeField()),
                ('status', models.CharField(max_length=1)),
                ('tipo', models.CharField(max_length=1)),
                ('valor', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('corretora_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.corretora')),
                ('ordem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.orderenvio')),
            ],
        ),
    ]
