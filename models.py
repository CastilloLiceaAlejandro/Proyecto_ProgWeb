class Producto(models.Model):
    ID_Juego=models.IntegerField(primary_key=true)
    Nombre_Juego=models.CharField(max_length=40)
    Plataforma=models.ForeignKey(Plataforma,on_delete=models.CASCADE)
    Genero=models.CharField(max_length=10)
    ESRB=models.CharField(max_length=10)
    Precio=models.IntegerField()
    Nombre_Desarrollador=models.ForeignKey(Desarrollador,on_delete=models.CASCADE)
    Fecha_Lanzamiento=models.DateField()
    Puntuacion=model.IntegerField()
    Alta_Producto=models.DateField()
    Actualizacion_Producto=DateTimeField(auto_now=true)


class Plataforma(models.Model):
    ID_Plataforma=models.IntegerField(primary_key=true)
    Plataforma=models.CharField(max_length=10)
    Empresa=models.CharField(max_length=20)
    CPU=models.CharField(max_length=30)
    Frecuencia_CPU=models.CharField(max_length=5)
    RAM=models.CharField(max_length=5)
    Memoria_Interna=models.CharField(max_length=4)
    Energia=models.CharField(max_length=10)

class Desarrollador(models.Model):
    ID_Desarrollador=models.IntegerField(primary_key=true)
    ID_Juego=models.ForeignKey(Producto,on_delete=models.CASCADE)
    Nombre_Desarrollador=models.CharField(max_length=10)

class Stock(models.Model):
    ID_Juego=models.ForeignKey(Producto,on_delete=models.CASCADE)
    Cantidad=models.IntegerField()
