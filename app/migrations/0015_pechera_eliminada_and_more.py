# Generated by Django 4.2.6 on 2023-11-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_cambiospechera'),
    ]

    operations = [
        migrations.AddField(
            model_name='pechera',
            name='eliminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pechera',
            name='indice_microbiologico',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, verbose_name='Índice Microbiológico'),
        ),
        migrations.AlterField(
            model_name='pechera',
            name='parameters',
            field=models.CharField(choices=[('1', 'Nuevo'), ('2', 'Perfectas condiciones'), ('3', 'Ligermante desgastanda'), ('4', 'Desgastada'), ('5', 'Eliminar')], default='1', max_length=50),
        ),
    ]
