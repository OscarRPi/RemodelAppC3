from django.db import models

class Producto(models.Model):
    Id_Producto= models.CharField(max_length=5, primary_key=True)
    Producto = models.CharField(max_length=50)
    Categoria = models.CharField(max_length= 50)
    
    def __str__(self):
        txt = "{0} {1} ({2})"
        return txt.format(self.Id_Producto,self.Producto,self.Categoria)

class Proveedor(models.Model):
    Id_Proveedor = models.CharField(max_length=5, primary_key=True)
    Proveedor = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Whatsapp = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    
    def __str__(self):
        txt = "{0} {1} ({2})"
        return txt.format(self.Id_Proveedor,self.Proveedor,self.Ciudad)

class Producto_Ingresado(models.Model):
    Id_ProductoIngresado = models.CharField(max_length=5, primary_key=True)
    Id_Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    Id_Proveedor = models.ForeignKey(Proveedor, null=False, blank=False,on_delete=models.CASCADE)
    Valor = models.DecimalField(max_digits=8, decimal_places=0, default=0.0)
    Color = models.CharField(max_length=50)
    Tipo_Material = models.CharField(max_length=50)
    Fecha_Ingreso = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.Id_ProductoIngresado,self.Id_Producto)
# Create your models here.
