# Generated by Django 2.2.4 on 2023-10-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTP1Reprise', '0011_auto_20231012_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnegrcntp1',
            name='prenom',
            field=models.CharField(default=1, max_length=200, verbose_name='Prénom'),
            preserve_default=False,
        ),
    ]