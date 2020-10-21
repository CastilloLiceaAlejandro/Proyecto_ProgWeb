from rest_framework import serializers

from Proyecto.models import Plataforma, Desarrollador, Producto, Stock

class PlataformaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = "__all__"
class PlataformaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ("ID_Plataforma", "Plataforma", "Empresa")


class DesarrolladorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = "__all__"


class ProductoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
class ProductoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("ID_Juego", "Nombre_Juego", "Plataforma", "Precio", "Puntuacion")


class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
