from django.db import models

class Trainer(models.Model):
    name= models.CharField(max_length=30, null= False)
    surname=models.CharField(max_length=30, null=False)
    Birthdate= models.DateField()
    level= models.IntegerField(default=1)
    picture= models.ImageField(upload_to="trainer_images",default='trainer_images')
   
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Pokemon (models.Model):
   name= models.CharField(max_length=30, null=False)
   POKEMON_TYPES ={
       ('A','Agua'),
       ('F','Fuego'),
       ('T','Tierra'),
       ('P','Planta'),
       ('E','Electrico'),
       
   }
   
   type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
   weight = models.DecimalField(decimal_places=2, max_digits=6)
   height = models.DecimalField(decimal_places=2, max_digits=6)
   Trainer = models.ForeignKey(Trainer,on_delete=models.SET_NULL, null=True)
   picture= models.ImageField(upload_to="pokemon_images",default='pokemon_images')


   def __str__(self):
        return self.name
   


