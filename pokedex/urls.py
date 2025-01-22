from django.urls import path
from lab8 import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'pokedex'

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/",views.trainer_details, name="trainer"),
    path("add_pokemon/", views.add_pokemon , name='add_pokemon'),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view, name="Login"),
    
    ]   

urlpatterns += static(settings.MEDIA_DRL, document_root=settings.MEDIA_ROOT)

