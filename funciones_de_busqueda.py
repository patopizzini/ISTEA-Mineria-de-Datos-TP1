import unicodedata

def normalizar(texto):
    texto = texto.lower()

    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def buscar_libros_por_genero(lista_libros, genero):
    libros_coincidentes = []
    for libro in lista_libros:
        if normalizar(libro.genero) == normalizar(genero):
            libros_coincidentes.append(libro.nombre)
        
    if not libros_coincidentes:
        print(f"No hay libros con ese genero.")
    else:
        print(f"\nLibros encontrados para el género '{genero}':")

        for libro in libros_coincidentes:
            print(f"• {libro}")

def libro_con_mayor_puntuacion_por_genero(lista_libros, genero):
    libro_con_puntuacion_mas_alta = ""
    puntuacion_mas_alta = float(0)
    
    for libro in lista_libros:
        if normalizar(libro.genero) == normalizar(genero):
            if libro.puntuacion > puntuacion_mas_alta:
                libro_con_puntuacion_mas_alta = libro.nombre
                puntuacion_mas_alta = libro.puntuacion

    if libro_con_puntuacion_mas_alta == "":
        print(f"No hay libros con ese genero.")
    else:
        print(f"El libro con mayor puntuación del genero {genero} es {libro_con_puntuacion_mas_alta}")