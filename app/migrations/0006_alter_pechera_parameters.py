# Generated by Django 4.2.6 on 2023-10-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_pechera_parameters_alter_pechera_planta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pechera',
            name='parameters',
            field=models.CharField(choices=[('1', 'Nuevo'), ('2', 'Perfectas condiciones'), ('3', 'Ligermante desgastanda'), ('4', 'Desgastada'), ('5', 'Eliminar')], default=1, max_length=50),
        ),
    ]
