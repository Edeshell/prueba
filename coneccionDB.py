import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sis11a-v-prueba"]
collection = db["peliculas"]


