# Generated by Django 3.2.8 on 2022-01-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220105_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corretora',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
