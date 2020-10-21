from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PlataformaListSerializer, DesarrolladorListSerializer, ProductoListSerializer, StockListSerializer
from .serializers import PlataformaDetailSerializer, ProductoDetailSerializer

from Proyecto.models import Plataforma, Desarrollador, Producto, Stock

# Create your views here.

class PlataformaList(APIView):
    def get(self,request):
        plataforma = Plataforma.objects.all()
        data = PlataformaListSerializer(plataforma , many = True).data
        return Response(data)
class PlataformaDetail(APIView):
    def get(self,request,pk):
        plataforma = get_object_or_404(Plataforma, pk = pk)
        data = PlataformaDetailSerializer(plataforma).data
        return Response(data)


class DesarrolladorList(APIView):
    def get(self,request):
        desarrollador = Desarrollador.objects.all()
        data = DesarrolladorSerializer(desarrollador , many = True).data
        return Response(data)


class ProductoList(APIView):
    def get(self,request):
        producto = Producto.objects.all()
        data = ProductoListSerializer(producto , many = True).data
        return Response(data)
class ProductoDetail(APIView):
    def get(self,request,pk):
        producto = get_object_or_404(Producto, pk = pk)
        data = ProductoDetailSerializer(producto).data
        return Response(data)


class StockList(APIView):
    def get(self,request):
        stock = Stock.objects.all()
        data = StockSerializer(stock , many = True).data
        return Response(data)
