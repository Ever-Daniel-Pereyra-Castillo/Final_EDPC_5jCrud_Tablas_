from django.shortcuts import render, redirect
from .models import Proveedores
# Create your views here.
def inicio_vistaProveedores(request):
    losProveedores=Proveedores.objects.all()
    return render(request,"gestionarProveedores.html", {"misProveedores":losProveedores}   )

def registrarProveedores(request):
    ID_proveedor=request.POST["numID_proveedor"]
    Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Empresa=request.POST["txtEmpresa"]
    Productos=request.POST["txtProductos"]
    Stock=request.POST["numStock"]
    Rfc=request.POST["txtRfc"]
    
    guardarProveedores=Proveedores.objects.create(
        ID_proveedor=ID_proveedor,Telefono=Telefono,Correo=Correo,Empresa=Empresa,Productos=Productos,Stock=Stock,Rfc=Rfc
    ) #GUARDA EL REGISTRO
    
    return redirect("proveedores")

def seleccionarProveedores(request,ID_proveedor):
    proveedores=Proveedores.objects.get(ID_proveedor=ID_proveedor)
    return render(request, "editarProveedores.html",{"misProveedores":proveedores})

def editarProveedores(request):
    ID_proveedor=request.POST["numID_proveedor"]
    Telefono=request.POST["numTelefono"]
    Correo=request.POST["txtCorreo"]
    Empresa=request.POST["txtEmpresa"]
    Productos=request.POST["txtProductos"]
    Stock=request.POST["numStock"]
    Rfc=request.POST["txtRfc"]
    proveedores=Proveedores.objects.get(ID_proveedor=ID_proveedor)
    proveedores.Telefono=Telefono
    proveedores.Correo=Correo
    proveedores.Empresa=Empresa
    proveedores.Productos=Productos
    proveedores.Stock=Stock
    proveedores.Rfc=Rfc
    
    proveedores.save() #guarda registro actualizado
    return redirect("proveedores")

def borrarProveedores(request,ID_proveedor):
    proveedores=Proveedores.objects.get(ID_proveedor=ID_proveedor)
    proveedores.delete() # borra el registro
    return redirect("proveedores")