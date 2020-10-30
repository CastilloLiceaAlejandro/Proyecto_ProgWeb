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
class PlataformaNewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Plataforma.objects.create(**validated_data)
    class Meta:
        model = Plataforma
        fields = "__all__"


class DesarrolladorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = "__all__"
class DesarrolladorNewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Desarrollador.objects.create(**validated_data)
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
class ProductoNewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Producto.objects.create(**validated_data)
    class Meta:
        model = Producto
        fields = "__all__"


class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
class StockNewSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Stock.objects.create(**validated_data)
    class Meta:
        model = Stock
        fields = "__all__"
