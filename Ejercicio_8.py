class Libro:
    def __init__(self):
        self.titulo = input("Ingrese el título del libro: ")
        self.autor = input("Ingrese el nombre del autor: ")
        self.año_publicacion = int(input("Ingrese el año de publicación: "))
        self.genero = input("Ingrese el género del libro: ")

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")
        print(f"Género: {self.genero}")

    def recomendar(self):
        print(f"¡Recomiendo el libro '{self.titulo}' de {self.autor}!")