from django.db import models

# Create your models here.
class Ventas(models.Model):
    ID_venta = models.PositiveBigIntegerField(null=False, primary_key=True)
    Precio = models.PositiveBigIntegerField(null=False)
    Fecha = models.DateField(null=False)
    ID_Producto = models.PositiveBigIntegerField(null=False)
    ID_Cliente = models.PositiveBigIntegerField(null=False)
    ID_Empleado = models.PositiveBigIntegerField(null=False)
    ID_Sucursal = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return self.Nombre