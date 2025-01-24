from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer
from pokedex.forms import PokemonForm
from pokedex.forms import TrainerForm
from django.shortcuts import redirect , render
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


        
def trainers(request,trainer_id):
    trainers=Trainer.objects.all()
    template= loader.get_template




def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id= pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))
    

def edit_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.post,request.FILES)
        if form.is_valid():
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html' , {'form': form})



def trainer_details(request,trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context= {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))
@login_required
def add_pokemon(request,pokemon_id):
    pokemon= Pokemon.objects.get(id=pokemon_id)
    if request.method=="POST":
        form= PokemonForm(request.POST, request.FILES)
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


class CustomLoginView(LoginView):
    template_name = 'login_form.html'

def add_trainer(request):
    if request.method =="POST":
        Form= Trainerform(request.POST,request.Files)
        if form.is_valid():
           form.save() 
           return redirect('pokedex:index')
       
def edit_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html' , {'form': form})

