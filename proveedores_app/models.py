from django.db import models

# Create your models here.
class Proveedores(models.Model):
    ID_proveedor = models.PositiveBigIntegerField(null=False, primary_key=True)
    Telefono = models.PositiveBigIntegerField(null=False)
    Correo = models.CharField(max_length=50,null=False)
    Empresa = models.CharField(max_length=50, null=False)
    Productos= models.CharField(max_length=500,null=False)
    Stock = models.PositiveBigIntegerField(null=False)
    Rfc = models.CharField(max_length=20,null=False)