# Generated by Django 5.0.2 on 2024-02-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('data_expiracao', models.DateField(verbose_name='data_expiracao')),
            ],
        ),
    ]
