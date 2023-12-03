class Phone:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False
        self.bateria_porcentaje = 100

    def encender_apagar(self):
        self.encendido = not self.encendido
        if self.encendido:
            print("¡Teléfono encendido!")
        else:
            print("Teléfono apagado.")

    def verificar_bateria(self):
        print(f"Nivel de batería: {self.bateria_porcentaje}%")

    def cargar_bateria(self, porcentaje):
        self.bateria_porcentaje = min(100, self.bateria_porcentaje + porcentaje)
        print(f"Batería cargada. Nivel actual: {self.bateria_porcentaje}%")

    def llamar(self, numero):
        if self.encendido and self.bateria_porcentaje > 0:
            print(f"Llamando al número {numero}...")
            self.bateria_porcentaje -= 20
        elif not self.encendido:
            print("El teléfono está apagado. Enciéndelo para realizar una llamada.")
        else:
            print("Batería demasiado baja. Carga el teléfono antes de realizar una llamada.")