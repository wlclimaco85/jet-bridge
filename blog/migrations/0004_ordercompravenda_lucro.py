# Generated by Django 3.2.8 on 2022-03-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220315_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercompravenda',
            name='lucro',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
