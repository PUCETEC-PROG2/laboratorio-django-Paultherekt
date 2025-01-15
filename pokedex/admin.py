from django.contrib import admin
from .models import Pokemon
from .models import trainer

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass 

@admin.register(trainer)
class trainerAdmin(admin.ModelAdmin):
    pass
