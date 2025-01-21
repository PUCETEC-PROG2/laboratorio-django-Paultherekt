from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer
from pokedex.forms import PokemonForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
def index(request):
    pokemons= Pokemon.objects.all()
    trainers= Trainer.objects.all()
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
    

def edit_pokemon(request,pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == "post":
        form = PokemonForm(request.post,request.FILES)
        if form.is_valid():
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html' , {'form': form})
@login_required

def trainer_details(request,trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context= {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method=="post":
        form= PokemonForm(request.post, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form':form})
@login_required

def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id= pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')
@login_required
def as_view(request):
    template= loader.get_template('login_form.html')
    context= {
            
        'form': form
     }
        
