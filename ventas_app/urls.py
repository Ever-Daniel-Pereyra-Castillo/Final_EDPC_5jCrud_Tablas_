from django.urls import path
from ventas_app import views
urlpatterns = [
    path("ventas", views.inicio_vistaVentas, name= "ventas" ),
    path("registrarVentas/",views.registrarVentas,name="registrarVentas"),
    path("seleccionarVentas/<ID_venta>",views.seleccionarVentas,name="seleccionarVentas"),
    path("editarVentas/",views.editarVentas,name="editarVentas"),
    path("borrarVentas/<ID_venta>",views.borrarVentas,name="borrarVentas")
]