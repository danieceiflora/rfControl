# Generated by Django 5.1.4 on 2025-02-08 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfs', '0008_cadastroleitura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastroleitura',
            name='horaLeitura',
        ),
        migrations.AlterField(
            model_name='cadastroleitura',
            name='idEquipamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rfs.cadastroequipamento', verbose_name='Equipamento'),
        ),
    ]
