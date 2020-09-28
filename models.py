from django.db import models

# Create your models here.

class Plataforma(models.Model):
    ID_Plataforma=models.IntegerField(primary_key=True)
    Plataforma=models.CharField(max_length=10)
    Empresa=models.CharField(max_length=20)
    CPU=models.CharField(max_length=30)
    Frecuencia_CPU=models.CharField(max_length=10)
    RAM=models.CharField(max_length=10)
    Memoria_Interna=models.CharField(max_length=10)
    Energia=models.CharField(max_length=10)
    def __str__(self):
        return self.Plataforma

class Desarrollador(models.Model):
    ID_Desarrollador=models.IntegerField(primary_key=True)
    Nombre_Desarrollador=models.CharField(max_length=10)
    def __str__(self):
        return self.Nombre_Desarrollador

class Producto(models.Model):
    ID_Juego=models.IntegerField(primary_key=True)
    Nombre_Juego=models.CharField(max_length=40)
    Plataforma=models.ForeignKey(Plataforma,on_delete=models.CASCADE)
    Genero=models.CharField(max_length=10)
    ESRB=models.CharField(max_length=10)
    Precio=models.IntegerField()
    Nombre_Desarrollador=models.ForeignKey(Desarrollador,on_delete=models.CASCADE)
    Fecha_Lanzamiento=models.DateField()
    Puntuacion=models.IntegerField()
    Alta_Producto=models.DateField()
    Actualizacion_Producto=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Nombre_Juego

class Stock(models.Model):
    ID_Juego=models.ForeignKey(Producto,on_delete=models.CASCADE)
    Cantidad=models.IntegerField()
    def __str__(self):
        return self.ID_Juego
