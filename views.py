from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Producto
from .models import Desarrollador
from .models import Plataforma
from .models import Stock

class List(generic.ListView):
    template_name = "proyecto/list.html"
    model = Producto
