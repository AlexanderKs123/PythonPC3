
def dividire(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None

def mostrar_menus():
    print("Menú:")
    print("1. Dividir dos números")
    print("0. Salir")