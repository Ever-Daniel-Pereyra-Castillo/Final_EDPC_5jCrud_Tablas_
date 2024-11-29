from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.
def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all()
    return render(request,"gestionarVentas.html", {"misVentas":lasVentas}   )

def registrarVentas(request):
    ID_venta=request.POST["numID_venta"]
    Precio=request.POST["numPrecio"]
    Fecha=request.POST["datFecha"]
    ID_Producto=request.POST["numID_Producto"]
    ID_Cliente=request.POST["numID_Cliente"]
    ID_Empleado=request.POST["numID_Empleado"]
    ID_Sucursal=request.POST["numID_Sucursal"]
    
    guardarVentas=Ventas.objects.create(
        ID_venta=ID_venta,Precio=Precio,Fecha=Fecha,ID_Producto=ID_Producto,ID_Cliente=ID_Cliente,ID_Empleado=ID_Empleado,ID_Sucursal=ID_Sucursal
    ) #GUARDA EL REGISTRO
    
    return redirect("ventas")

def seleccionarVentas(request,ID_venta):
    ventas=Ventas.objects.get(ID_venta=ID_venta)
    return render(request, "editarVentas.html",{"misVentas":ventas})

def editarVentas(request):
    ID_venta=request.POST["numID_venta"]
    Precio=request.POST["numPrecio"]
    Fecha=request.POST["datFecha"]
    ID_Producto=request.POST["numID_Producto"]
    ID_Cliente=request.POST["numID_Cliente"]
    ID_Empleado=request.POST["numID_Empleado"]
    ID_Sucursal=request.POST["numID_Sucursal"]
    ventas=Ventas.objects.get(ID_venta=ID_venta)
    ventas.Precio=Precio
    ventas.Fecha=Fecha
    ventas.ID_Producto=ID_Producto
    ventas.ID_Cliente=ID_Cliente
    ventas.ID_Empleado=ID_Empleado
    ventas.ID_Sucursal=ID_Sucursal
    
    ventas.save() #guarda registro actualizado
    return redirect("ventas")

def borrarVentas(request,ID_venta):
    ventas=Ventas.objects.get(ID_venta=ID_venta)
    ventas.delete() # borra el registro
    return redirect("ventas")