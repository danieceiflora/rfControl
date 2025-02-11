# Generated by Django 5.1.4 on 2025-02-08 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfs', '0007_instalacaosensor_data_remocao_sensor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroLeitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataLeitura', models.DateTimeField(verbose_name='Data da Leitura')),
                ('horaLeitura', models.TimeField(verbose_name='Hora da Leitura')),
                ('leitura', models.FloatField(verbose_name='Leitura')),
                ('idEquipamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rfs.cadastroequipamento', verbose_name='Id do Equipamento')),
                ('idSensor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rfs.cadastrosensor', verbose_name='Sensor')),
            ],
            options={
                'verbose_name': 'Leitura',
                'verbose_name_plural': 'Leituras',
            },
        ),
    ]
