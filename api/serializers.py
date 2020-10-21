from rest_framework import serializers

from Proyecto.models import Plataforma, Desarrollador, Producto, Stock

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = "__all__"

class DesarrolladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
