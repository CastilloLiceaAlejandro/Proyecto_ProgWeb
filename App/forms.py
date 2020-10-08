from django import forms

from .models import Producto
from .models import Plataforma

class FormCreate_Producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class FormCreate_Plataforma(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = "__all__"
