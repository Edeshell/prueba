
from crud import  *
from  funciones import *
while True:
    print("\n---Menu de opciones---\n")
    print("1- Mostrar catalogo")
    print("2- Buscar pelicula")
    print("3- Agregar pelicula")
    print("4- Modificar pelicula")
    print("5- Eliminar pelicula")
    print("6- Salir del programa")

    opcion = input("ingrese una opcion: ")
    if opcion == "1":
        mostrar_pelis()

    elif opcion == "2":
        title = str(input("ingresa el titulo de la pelicula: "))
        mostrar_titulo(title)

    elif opcion == "3":
        peliculas = insertar_pelicula()
        crear_peli(peliculas)

    elif opcion == "4":
        title = str(input("ingresa el titulo de la pelicula a modificar: "))
        peliculas = json_actualizar_peli()
        actualizar_peli(title, peliculas)

    elif opcion == "5":
        title = str(input("ingresa el titulo de la pelicula a eliminar: "))
        peliculas = eliminar_peli(title)
    elif opcion == "6":
        break