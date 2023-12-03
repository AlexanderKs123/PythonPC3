from Ejercicio_2 import Circulo
from Ejercicio_3 import Producto, Catalogo

# RESOLUCION DEL EJERCICIO_2
if __name__ == "__main__":

    # RESOLUCION DEL EJERCICIO_2
    radio_circulo = 3
    mi_circulo = Circulo(radio_circulo)
    area_del_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {radio_circulo} es: {area_del_circulo}")


   # RESOLUCION DEL EJERCICIO_3
    catalogo_tienda = Catalogo()
    producto5 = Producto(codigo=5, nombre="Filtros", precio=99.99)
    producto6 = Producto(codigo=6, nombre="Bateria", precio=19.99)
    catalogo_tienda.agregar_producto(producto5)
    catalogo_tienda.agregar_producto(producto6)
    catalogo_tienda.mostrar_catalogo()