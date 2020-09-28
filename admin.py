from django.contrib import admin

from .models import Producto
from .models import Desarrollador
from .models import Plataforma
from .models import Stock
# Register your models here.

admin.site.register(Producto)
admin.site.register(Desarrollador)
admin.site.register(Plataforma)
admin.site.register(Stock)
