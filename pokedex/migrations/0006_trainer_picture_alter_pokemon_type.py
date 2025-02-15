# Generated by Django 4.2 on 2025-01-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_alter_pokemon_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='picture',
            field=models.ImageField(default='trainer_images', upload_to='trainer_images'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('E', 'Electrico'), ('A', 'Agua'), ('T', 'Tierra'), ('P', 'Planta'), ('F', 'Fuego')], max_length=30),
        ),
    ]
