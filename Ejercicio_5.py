class Productos:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def identificar_pais_lote(self):
        # Separar el código en partes usando el guion "-"
        partes_codigo = self.codigo.split('-')

        # Verificar si hay al menos tres partes
        if len(partes_codigo) >= 3:
            pais = partes_codigo[0]
            lote = partes_codigo[1]
            año = partes_codigo[2]

            return f"País: {pais}, Número de Lote: {lote}, Año: {año}"
        else:
            return "Formato de código incorrecto."

    def __str__(self):
        return f"Producto(nombre={self.nombre}, codigo={self.codigo})"