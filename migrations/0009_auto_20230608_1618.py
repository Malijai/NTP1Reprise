# Generated by Django 2.2.4 on 2023-06-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NTP1Reprise', '0008_auto_20230608_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='amende_type',
            field=models.ForeignKey(blank=True, default=998, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='NTP1Reprise.Type', verbose_name="Caractéristiques de l'amende"),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='uniteprobation',
            field=models.ForeignKey(blank=True, default=998, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='duree_probation', to='NTP1Reprise.Duree', verbose_name='Jours, mois, ans etc?'),
        ),
    ]