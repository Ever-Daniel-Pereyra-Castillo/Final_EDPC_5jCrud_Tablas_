from django.db import models

# Create your models here.
class Productos(models.Model):
    ID_producto = models.PositiveBigIntegerField(null=False, primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)
    Calorias = models.PositiveBigIntegerField(null=False)
    Vitaminas = models.CharField(max_length=20, null=False)
    Precio = models.PositiveBigIntegerField(null=False)
    Stock = models.PositiveBigIntegerField(null=False)
    ID_Proveedor = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return self.Nombre