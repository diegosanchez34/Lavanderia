# Generated by Django 5.0.2 on 2024-04-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_planta_cantidad_planta_kilos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='planta',
            name='kilos',
            field=models.IntegerField(default=0),
        ),
    ]