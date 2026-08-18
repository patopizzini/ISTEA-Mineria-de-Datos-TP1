class Libro:
    def __init__(self, nombre, autor, genero, puntuacion):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Autor: {self.autor}\n"
            f"Género: {self.genero}\n"
            f"Puntuación: {self.puntuacion}"
        )