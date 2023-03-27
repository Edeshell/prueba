def insertar_pelicula():
    titulo = input("Titulo: ")
    fecha = int(input("Fecha: "))
    genero = input("Genero: ")
    print("Pelicula insertada correctamente")

    peliculas = {
        "titulo": titulo,
        "fecha": fecha,
        "genero": genero
    }
    return peliculas


def json_actualizar_peli():
    print("Menu de opciones")
    print("1- Modificar todos los datos de la pelicula")
    print("2- Modificar solo un elemento")

    opcion = input("Ingresa una opcion: ")
    if opcion == "1":
        return insertar_pelicula()
    elif opcion == "2":
        indice = input("Ingresa el indice a buscar: ")
        valor = input("Ingresa el valor a modificar: ")
        peliculas = {indice: valor}
        return peliculas


