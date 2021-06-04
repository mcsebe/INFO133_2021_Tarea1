from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['Tarea']
collection = db['Usuarios']
x = True


collection.insert_one({ 
	"RUT": Rut,
	"nombre": nombre,
	"apellido": apellido,
	"Archivo_Audio" : [{ 
			"ID_archivo" : None,
			"formato" : None,
			"exterior" : None,
			"fecha_grabacion" : None,
			"duracion" : None,
			"longitud" : None,
			"latitud" : None,
			"ciudad" : None,
			"fecha upload" : None,
			"RUT_Usuario" : None,
			"Segmentos" : [{
				"ID_segmento" : None,
				"formato" : None,
				"duracion" : None,
				"inicio" : None,
				"fin" : None,
				"ID_archivo" : None
			}]
		}]
})

collection = db['Fuentes']
collection.insert_one({ 
	"nombre_fuente": None,
	"descripción": None,
	"nombre_super_categoria": None
})

collection = db['Analizar']
collection.insert_one({ 
	"nombre" : None,
	"ID_segmento" : None,
	"nombre_fuente" : None,
	"porcentaje" : None
})
