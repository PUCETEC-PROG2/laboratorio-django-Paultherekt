# Generated by Django 4.2 on 2025-01-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('F', 'Fuego'), ('P', 'Planta'), ('T', 'Tierra'), ('E', 'Electrico'), ('A', 'Agua')], max_length=30),
        ),
    ]
