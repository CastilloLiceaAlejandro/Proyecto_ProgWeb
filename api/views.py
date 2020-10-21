from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PlataformaSerializer, DesarrolladorSerializer, ProductoSerializer, StockSerializer

from Proyecto.models import Plataforma, Desarrollador, Producto, Stock

# Create your views here.

class PlataformaList(APIView):
    def get(self,request):
        plataforma = Plataforma.objects.all()
        data = PlataformaSerializer(plataforma , many = True).data
        return Response(data)

class DesarrolladorList(APIView):
    def get(self,request):
        desarrollador = Desarrollador.objects.all()
        data = DesarrolladorSerializer(desarrollador , many = True).data
        return Response(data)

class ProductoList(APIView):
    def get(self,request):
        producto = Producto.objects.all()
        data = ProductoSerializer(producto , many = True).data
        return Response(data)

class StockList(APIView):
    def get(self,request):
        stock = Stock.objects.all()
        data = StockSerializer(stock , many = True).data
        return Response(data)
