# Generated by Django 4.2 on 2025-01-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('A', 'Agua'), ('T', 'Tierra'), ('E', 'Electrico'), ('F', 'Fuego'), ('P', 'Planta')], max_length=30),
        ),
    ]
