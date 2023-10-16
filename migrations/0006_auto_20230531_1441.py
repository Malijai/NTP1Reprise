# Generated by Django 2.2.4 on 2023-05-31 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NTP1Reprise', '0005_auto_20230526_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='amendecout',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Cout total de l'amende"),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='consecutifsON',
            field=models.BooleanField(verbose_name='Consécutif? Cocher si oui'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='detentionduree',
            field=models.IntegerField(blank=True, default=0, max_length=50, null=True, verbose_name='Durée de la détention'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='interdictionduree',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Durée de l'interdiction"),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='probationduree',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Durée de la probation'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='surcisduree',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Durée du surcis'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='unitedetention',
            field=models.ForeignKey(blank=True, default=998, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='duree_detention', to='NTP1Reprise.Duree', verbose_name='Jours, mois, ans etc?'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='uniteinterdiction',
            field=models.ForeignKey(blank=True, default=998, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='duree_interdiction', to='NTP1Reprise.Duree', verbose_name='Jours, mois, ans etc?'),
        ),
        migrations.AlterField(
            model_name='nouveauxdelitsntp1',
            name='unitesurcis',
            field=models.ForeignKey(blank=True, default=998, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='duree_surcis', to='NTP1Reprise.Duree', verbose_name='Jours, mois, ans etc?'),
        ),
    ]