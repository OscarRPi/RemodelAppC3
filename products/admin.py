from django.contrib import admin

from .models import Proveedor

admin.site.register(Proveedor)

from .models import Producto

admin.site.register(Producto)

from .models import Producto_Ingresado

admin.site.register(Producto_Ingresado)

# Register your models here.
