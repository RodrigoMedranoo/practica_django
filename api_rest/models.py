from django.db import models

# Create your models here.
class Comida (models.Model):
    nombre=models.CharField(max_length= 30)
    caloria=models.IntegerField()
    origen=models.CharField(max_length= 30)
    ingredientes=models.TextField()
    creado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}--{self.creado}"
    
class Bebida (models.Model):
    nombre=models.CharField(max_length= 30)
    sabor = models.CharField(max_length= 30)
    alcholico=models.BooleanField()
    cantidad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre}--{self.creado}"
    

class Dulces (models.Model):
    nombre=models.CharField(max_length= 30)
    sabor = models.CharField(max_length= 30)
    Empaque = models.CharField(max_lenght= 30)
    cantidad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre}--{self.creado}"
    
class Electronicos (models.Model):
    precio = models.CharField(max_lenght= 30)
    tipo = models.CharField(max_leght = 30)
    marca = models.CharField(max_leght = 30)
    
    def __str__(self):
        return f"{self.nombre}--{self.creado}"