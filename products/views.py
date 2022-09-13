import json
from django.http import JsonResponse
from django.views import View
from .models import Producto_Ingresado
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #Para enviar al cliente
    def get(self,request,id=0):
        if (id>0):
            products = list(Producto_Ingresado.objects.filter(Id_ProductoIngresado=id).values())
            if( len(products) > 0 ):
                product=products[0]
                datos = {'message':"Success",'products':product}
            else:
                datos = {'message':"Product not found..."}    
        else:
            products = list(Producto_Ingresado.objects.values())
            if len(products)>0:
                datos = {'message':"Success",'products':products}
            else:
                datos = {'message':"Products not found..."}
        return JsonResponse(datos)
    
    # Para recibir datos desde el cliente y crear un nuevo registro
    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Producto_Ingresado.objects.create(
            Valor=jd['Valor'],
            Color=jd['Color'],
            Tipo_Material=jd['Tipo_Material'],
            Fecha_Ingreso=jd['Fecha_Ingreso']
        )
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    # Para recibir datos desde el cliente y actualizar un registro    
    def put(self,request, id):
        jd = json.loads(request.body)
        products = list(Producto_Ingresado.objects.filter(Id_ProductoIngresado=id).values())
        if( len(products) > 0 ):
            product = Producto_Ingresado.objects.get(Id_ProductoIngresado=id)
            product.Valor = jd['Valor']
            product.Color = jd['Color']
            product.Tipo_Material = jd['Tipo_Material']
            product.Fecha_Ingreso = jd['Fecha_Ingreso']
            product.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Product not found..."}  
        return JsonResponse(datos)
    
    # Para recibir una orden desde el cliente y eliminar 
    def delete(self,request, id):
        products = list(Producto_Ingresado.objects.filter(Id_ProductoIngresado=id).values())
        if( len(products) > 0 ):
            Producto_Ingresado.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Product not found..."}
        return JsonResponse(datos)  
            

