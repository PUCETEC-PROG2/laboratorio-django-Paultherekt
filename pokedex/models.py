from django.db import models

class trainer(models.Model):
    name= models.CharField(max_length=30, null= False)
    surname=models.CharField(max_length=30, null=False)
    level= models.IntegerField(default=1)
    Birthdate= models.DateField()

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
   trainer = models.ForeignKey(trainer,on_delete=models.SET_NULL, null=True)

   def __str__(self):
        return self.name
   


