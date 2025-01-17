from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import trainer
def index(request):
    pokemons= Pokemon.objects.all()
    trainers= trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons , 
        'trainers': trainers
        } , request))


        
def trainers(request):
    trainers=trainer.objects.all()
    template= loader.get_template




def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id= pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_details(request,trainer_id):
    trainer = trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context= {
        'trainer': pokemon
    }
    return HttpResponse(template.render(context, request))
