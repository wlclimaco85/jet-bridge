# Generated by Django 3.2.8 on 2021-12-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_ordercompravenda_corretora_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercompravenda',
            name='corretora_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.corretora'),
        ),
    ]
