from django.contrib import admin
from .models import Proveedor
from .models import Producto
from .models import Producto_Ingresado

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Producto_Ingresado)

# Register your models here.
