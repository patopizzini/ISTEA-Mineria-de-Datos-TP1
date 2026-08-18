import csv

def agregar_nuevo_libro_a_csv(ruta, nombre, autor, genero, puntuacion):
    with open(ruta, mode='r', encoding='utf-8') as f:
        contenido = f.read()
        necesita_salto = len(contenido) > 0 and not contenido.endswith('\n')

    with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
        if necesita_salto:
            archivo.write('\n')
            
        writer = csv.writer(archivo, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow([nombre, autor, genero, float(puntuacion)])