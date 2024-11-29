from django.shortcuts import render, redirect
from .models import Productos
# Create your views here.
def inicio_vistaProductos(request):
    losProductos=Productos.objects.all()
    return render(request,"gestionarProductos.html", {"misProductos":losProductos}   )

def registrarProductos(request):
    ID_producto=request.POST["numID_producto"]
    Nombre=request.POST["txtNombre"]
    Calorias=request.POST["numCalorias"]
    Vitaminas=request.POST["txtVitaminas"]
    Precio=request.POST["numPrecio"]
    Stock=request.POST["numStock"]
    ID_Proveedor=request.POST["numID_Proveedor"]
    
    guardarProductos=Productos.objects.create(
        ID_producto=ID_producto,Nombre=Nombre,Calorias=Calorias,Vitaminas=Vitaminas,Precio=Precio,Stock=Stock,ID_Proveedor=ID_Proveedor
    ) #GUARDA EL REGISTRO
    
    return redirect("productos")

def seleccionarProductos(request,ID_producto):
    productos=Productos.objects.get(ID_producto=ID_producto)
    return render(request, "editarProductos.html",{"misProductos":productos})

def editarProductos(request):
    ID_producto=request.POST["numID_producto"]
    Nombre=request.POST["txtNombre"]
    Calorias=request.POST["numCalorias"]
    Vitaminas=request.POST["txtVitaminas"]
    Precio=request.POST["numPrecio"]
    Stock=request.POST["numStock"]
    ID_Proveedor=request.POST["numID_Proveedor"]
    productos=Productos.objects.get(ID_producto=ID_producto)
    productos.Nombre=Nombre
    productos.Calorias=Calorias
    productos.Vitaminas=Vitaminas
    productos.Precio=Precio
    productos.Stock=Stock
    productos.ID_Proveedor=ID_Proveedor
    
    productos.save() #guarda registro actualizado
    return redirect("productos")

def borrarProductos(request,ID_producto):
    productos=Productos.objects.get(ID_producto=ID_producto)
    productos.delete() # borra el registro
    return redirect("productos")