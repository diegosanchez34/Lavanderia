# Generated by Django 4.2.6 on 2023-11-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_pechera_eliminada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pechera',
            name='historial',
            field=models.JSONField(default=list),
        ),
    ]
