from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy

from .models import Producto
from .models import Plataforma
from .models import Desarrollador
from .models import Stock

from .forms import FormCreate

# Create your views here.

class Lista_Producto(generic.ListView):
	template_name = "inv/Lista_Producto.html"
	model = Producto

class Detail_Producto(generic.DetailView):
	template_name = "inv/Detail_Producto.html"
	model = Producto

class New_Producto(generic.CreateView):
	template_name = "inv/New_Producto.html"
	model = Producto
	form_class = FormCreate
	success_url = reverse_lazy("inv:list")

class Update_Producto(generic.UpdateView):
	template_name = "inv/Update_Producto.html"
	model = Producto
	form_class = FormCreate
	success_url = reverse_lazy("inv:list")

class Delete_Producto(generic.DeleteView):
	template_name = "inv/Delete_Producto.html"
	model = Producto
	form_class = FormCreate
	success_url = reverse_lazy("inv:list")
