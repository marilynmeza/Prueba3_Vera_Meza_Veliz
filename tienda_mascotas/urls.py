from django.urls import path
from .views import inicio,cards,productos_stock,alimentos, \
    valida,venta,crear,eliminar, modificar,registrar


urlpatterns=[
    path('', inicio, name="inicio"),
    path('cards/', cards, name="cards"),
    path('productos_stock/', productos_stock, name="productos_stock"),
    path('alimentos/', alimentos, name="alimentos"),
    path('valida/', valida, name="valida"),
    path('venta/', venta, name="venta"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>',eliminar,name="eliminar"),
    path('modificar/<id>',modificar,name="modificar"),
    path('registro/',registrar,name="registro"),
]