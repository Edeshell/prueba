from coneccionDB import collection
#Mostrar todas las peliculas disponibles
def mostrar_pelis(id = None):
    if id is None:
        titulo = collection.find()
        for titulo in titulo:
            print(titulo)
    else:
        query = {"_id": id}
        titulo = collection.find_one(query)
        print(titulo)

#Buscar peliculas por su titulo
def mostrar_titulo(titulo):
    title = collection.find_one({"titulo": titulo})
    if title:
        print(title)
    else:
        print("pelicula no encontrada")

#Insertar una nueva pelicula
def crear_peli(peliculas):
    result = collection.insert_one(peliculas)
    print(result.inserted_id)

#Modificar datos de una pelicula existente
def actualizar_peli(titulo, json_actualizar):
    query = {"titulo": titulo}
    new_values ={"$set": json_actualizar}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

#Eliminar peliculas por titulo
def eliminar_peli(titulo):
    eli = {"titulo": titulo}
    result = collection.delete_one(eli)
    print(result.deleted_count)