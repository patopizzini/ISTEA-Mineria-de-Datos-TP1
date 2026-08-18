from clase_libro import Libro
from funciones_de_busqueda import (buscar_libros_por_genero, libro_con_mayor_puntuacion_por_genero)
from guardado_en_base import (agregar_nuevo_libro_a_csv)
import csv

ruta_csv = "libros.csv"

with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
    listado = csv.reader(archivo)
    lista_libros = []

    for libro in listado:
        lista_libros.append(Libro(libro[0], libro[1], libro[2], float(libro[3])))

while True:
    texto = """Seleccione una opcion:
        0. Salir
        1. Agregar Libro
        2. Buscar Libro por Genero
        3. Recomendar Libro
        """
        
    try:
        opcion = int(input(texto))
    except ValueError:
        print("Debe ingresar un número.")
        continue
    
    
    if opcion not in (0, 1, 2, 3):
        print("Número inválido. Intente nuevamente.")
        continue
    
    if opcion == 0:
        break
    
    elif opcion == 1:
        nombre = input("Ingrese el nombre del libro: ").title()
        autor = input("Ingrese el autor del libro: ").title()
        genero = input("Ingrese el genero del libro: ").title()
        
        while True:
            try:
                puntuacion = float(input("Ingrese la puntuación del libro: "))
                break
            except ValueError:
                print("Debe ingresar un número.")
        
        lista_libros.append(Libro(nombre, autor, genero, puntuacion))
        agregar_nuevo_libro_a_csv(ruta_csv, nombre, autor, genero, puntuacion)
        
        print("Se agregó el libro correctamente.")
        
    elif opcion == 2:
        genero = str(input("Ingrese el genero a buscar: "))
        buscar_libros_por_genero(lista_libros, genero)
        print("\n")
        
    elif opcion == 3:
        genero = str(input("Ingrese su genero de interes: "))
        libro_con_mayor_puntuacion_por_genero(lista_libros, genero)
        print("\n")
