from django.db import models

class trainer(models.Model):
    name= models.CharField(max_length=30, null= False)
    surname=models.CharField(max_length=30, null=False)
    level= models.IntegerField(default=1)
    Birthdate= models.DateField()

        def _str_(self):
             return f"{self.name} {self.surname}"
    
class Pokemon (models.Model):
   name= models.CharField(max_length=30, null=False)
   type = models.CharField(max_length=30, null=False)
   weight = models.DecimalField(decimal_places=4, max_digits=6)
   height = models.DecimalField(decimal_places=4, max_digits=6)
   
   
        def __str__(self):
            return self.name
   


