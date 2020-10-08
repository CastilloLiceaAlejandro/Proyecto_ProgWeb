from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy

from .models import Producto
from .models import Plataforma
from .models import Desarrollador
from .models import Stock

from .forms import FormCreate_Producto
from .forms import FormCreate_Plataforma

# Create your views here.

class Lista_Producto(generic.ListView):
	template_name = "inv/Producto/Lista_Producto.html"
	model = Producto

class Lista_Plataforma(generic.ListView):
	template_name = "inv/Plataforma/Lista_Plataforma.html"
	model = Plataforma


									       ### CRUD PRODUCTO ###

class Detail_Producto(generic.DetailView):
	template_name = "inv/Producto/Detail_Producto.html"
	model = Producto

class New_Producto(generic.CreateView):
	template_name = "inv/Producto/New_Producto.html"
	model = Producto
	form_class = FormCreate_Producto
	success_url = reverse_lazy("inv:listproducto")

class Update_Producto(generic.UpdateView):
	template_name = "inv/Producto/Update_Producto.html"
	model = Producto
	form_class = FormCreate_Producto
	success_url = reverse_lazy("inv:listproducto")

class Delete_Producto(generic.DeleteView):
	template_name = "inv/Producto/Delete_Producto.html"
	model = Producto
	form_class = FormCreate_Producto
	success_url = reverse_lazy("inv:listproducto")



									       ### CRUD PLATAFORMA ###

class Detail_Plataforma(generic.DetailView):
	template_name = "inv/Plataforma/Detail_Plataforma.html"
	model = Plataforma

class New_Plataforma(generic.CreateView):
	template_name = "inv/Plataforma/New_Plataforma.html"
	model = Plataforma
	form_class = FormCreate_Plataforma
	success_url = reverse_lazy("inv:listplataforma")

class Update_Plataforma(generic.UpdateView):
	template_name = "inv/Plataforma/Update_Plataforma.html"
	model = Plataforma
	form_class = FormCreate_Plataforma
	success_url = reverse_lazy("inv:listplataforma")

class Delete_Plataforma(generic.DeleteView):
	template_name = "inv/Plataforma/Delete_Plataforma.html"
	model = Plataforma
	form_class = FormCreate_Plataforma
	success_url = reverse_lazy("inv:listplataforma")
