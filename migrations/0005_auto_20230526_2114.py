# Generated by Django 2.2.4 on 2023-05-27 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTP1Reprise', '0004_auto_20230526_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='amendecout',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Cout total de l'amende"),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='detentionduree',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Durée de la détention'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='interdictionduree',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Durée de l'interdiction"),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='probationduree',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Durée de la probation'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='surcisduree',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Durée du surcis'),
        ),
    ]
