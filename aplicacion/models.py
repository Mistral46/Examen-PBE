from django.db import models

# Create your models here.
#Usuarios(nombre,correo,password)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password =models.CharField(max_length=100)
    def __str__(self):
        return (self.body)

#Topicos(deportes, noticias)
class Topico(models.Model):
    deportes=models.CharField(max_length=100)
    noticias=models.CharField(max_length=256)
    def __str__(self):
            return (self.body)

#Post(nombre,comentarios,fecha)
class Post(models.Model):
     id_usuario=models.CharField(max_length=100) #usuario que comenta  
     texto=models.CharField(max_length=100)
     fecha=models.DateTimeField()
     def __str__(self):
          return (self.body)