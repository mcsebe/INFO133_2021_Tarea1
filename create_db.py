from pymongo import MongoClient
from add_wavfile import encode_audio

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['Tarea']
collection = db['Audios']


def AgegarDato(collection):
	collection.insert_many([
	{ 
		"ID_archivo" : 1,
		"sonido": encode_audio("impresora1.wav"),
		"formato" : "wav",
		"exterior" : "interior",
		"fecha_grabacion" : "30-06-2021",
		"duracion" : 60,
		"latitud" : -39.82298137383703,
		"longitud" : -73.24279073177289,
		"ciudad" : "Valdivia",
		"fecha upload" : "30-06-2021",
		"Usuario" : {
			"RUT": "22507458-5",
			"nombre": "Cesar",
			"apellido": "Gracia",
		},
		"Segmentos" : [{
			"ID_segmento" : 100,
			"formato" : "wav",
			"duracion" : 60,
			"inicio" : 0,
			"fin" : 60,
			"Analizar": [{
				"tipo_analizador" : "Humano",
				"porcentaje" : None,
				"nombre_fuente": "Impresora",
				"descripción": "Impresora laser",
				"nombre_fuente_categoria": "Mecanico"		
			},
			{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 90,
				"nombre_fuente": "Impresora",
				"descripción": "Impresora laser.",
				"nombre_fuente_categoria": "Mecanico"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 2,
		"sonido": encode_audio("auto2.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "25-06-2021",
		"duracion" : 63,
		"latitud" : -39.82768169317065,
		"longitud" : -73.24020215419479,
		"ciudad" : "Valdivia",
		"fecha upload" : "25-06-2021",
		"Usuario" : {
			"RUT": "15606233-2",
			"nombre": "Magdalena",
			"apellido": "Cobo",
		},
		"Segmentos" : [{
			"ID_segmento" : 101,
			"formato" : "wav",
			"duracion" : 63,
			"inicio" : 0,
			"fin" : 63,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 95,
				"nombre_fuente": "Auto",
				"descripción": "Auto encendiendo y arrancando.",
				"nombre_fuente_categoria": "Vehiculos"		
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 3,
		"sonido": encode_audio("lluvia3.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "28-06-2021",
		"duracion" : 66,
		"latitud" : -39.809651803554864,
		"longitud" : -73.25676351029286,
		"ciudad" : "Valdivia",
		"fecha upload" : "28-06-2021",
		"Usuario" : {
			"RUT": "20056044-2",
			"nombre": "Sagrario",
			"apellido": "Benavente",
		},
		"Segmentos" : [{
			"ID_segmento" : 102,
			"formato" : "wav",
			"duracion" : 66,
			"inicio" : 0,
			"fin" : 66,
			"Analizar": [{
				"tipo_analizador" : "Humano",
				"porcentaje" : None,
				"nombre_fuente": "Lluvia",
				"descripción": "Sonido de lluvia",
				"nombre_fuente_categoria": "Climáticos y Medio ambientales"		
			}]
		}]

	},

	{ 
		"ID_archivo" : 4,
		"sonido": encode_audio("viento4.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "27-06-2021",
		"duracion" : 29,
		"latitud" : -39.81877264264198,
		"longitud" : -73.24969819123932,
		"ciudad" : "Valdivia", 
		"fecha upload" : "27-06-2021",
		"Usuario" : {
			"RUT": "16751646-7",
			"nombre": "Karina",
			"apellido": "Mercado",
		},
		"Segmentos" : [{
			"ID_segmento" : 103,
			"formato" : "wav",
			"duracion" : 29,
			"inicio" : 0,
			"fin" : 29,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 94,
				"nombre_fuente": "Viento",
				"descripción": "Sonido de viento en una tormenta.",
				"nombre_fuente_categoria": "Climáticos y Medio ambientales"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 5,
		"sonido": encode_audio("sirena5.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "26-06-2021",
		"duracion" : 30,
		"latitud" : -39.82443658089787,
		"longitud" : -73.2271502531366,
		"ciudad" : "Valdivia", 
		"fecha upload" : "26-06-2021",
		"Usuario" : {
			"RUT": "14337124-7",
			"nombre": "Mauricio",
			"apellido": "Rovira",
		},
		"Segmentos" : [{
			"ID_segmento" : 104,
			"formato" : "wav",
			"duracion" : 30,
			"inicio" : 0,
			"fin" : 30,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 89,
				"nombre_fuente": "Sirena",
				"descripción": "Sonido sirena de bomberos.",
				"nombre_fuente_categoria": "Alertas"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 6,
		"sonido": encode_audio("motosierra6.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "30-06-2021",
		"duracion" : 46,
		"latitud" : -39.80492182672446,
		"longitud" : -73.25041036829789,
		"ciudad" : "Valdivia", 
		"fecha upload" : "30-06-2021",
		"Usuario" : {
			"RUT": "13959169-0",
			"nombre": "Alma",
			"apellido": "Lloret",
		},
		"Segmentos" : [{
			"ID_segmento" : 105,
			"formato" : "wav",
			"duracion" : 46,
			"inicio" : 0,
			"fin" : 46,
			"Analizar": [{
				"tipo_analizador" : "Humano",
				"porcentaje" : None,
				"nombre_fuente": "Motosierra",
				"descripción": "Sonido de motosierra cortando madera.",
				"nombre_fuente_categoria": "Mecanico"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 7,
		"sonido": encode_audio("perro7.wav"),
		"formato" : "wav",
		"exterior" : "interior",
		"fecha_grabacion" : "28-06-2021",
		"duracion" : 21,
		"latitud" : -39.83313732002285,
		"longitud" : -73.23865156445318,
		"ciudad" : "Valdivia", 
		"fecha upload" : "28-06-2021",
		"Usuario" : {
			"RUT": "18122610-2",
			"nombre": "Lluc",
			"apellido": "Simon",
		},
		"Segmentos" : [{
			"ID_segmento" : 106,
			"formato" : "wav",
			"duracion" : 21,
			"inicio" : 0,
			"fin" : 21,
			"Analizar": [{
				"tipo_analizador" : "Humano",
				"porcentaje" : None,
				"nombre_fuente": "Perro",
				"descripción": "Perro ladrando al interior de una casa.",
				"nombre_fuente_categoria": "Animales"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 8,
		"sonido": encode_audio("pajaro8.wav"),
		"formato" : "wav",
		"exterior" : "exterior",
		"fecha_grabacion" : "27-06-2021",
		"duracion" : 49,
		"latitud" : -39.80196201802745,
		"longitud" : -73.26103097922493,
		"ciudad" : "Valdivia", 
		"fecha upload" : "27-06-2021",
		"Usuario" : {
			"RUT": "16958401-k",
			"nombre": "Graciela",
			"apellido": "Dorado",
		},
		"Segmentos" : [{
			"ID_segmento" : 107,
			"formato" : "wav",
			"duracion" : 49,
			"inicio" : 0,
			"fin" : 49,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 97,
				"nombre_fuente": "Pajaro",
				"descripción": "Sonido de pajaro en el bosque.",
				"nombre_fuente_categoria": "Animales"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 9,
		"sonido": encode_audio("restaurant9.wav"),
		"formato" : "wav",
		"exterior" : "interior",
		"fecha_grabacion" : "25-06-2021",
		"duracion" : 76,
		"latitud" : -39.815068229211036,
		"longitud" : -73.24639439075622,
		"ciudad" : "Valdivia", 
		"fecha upload" : "25-06-2021",
		"Usuario" : {
			"RUT": "12450795-2",
			"nombre": "Candida",
			"apellido": "Alcazar",
		},
		"Segmentos" : [{
			"ID_segmento" : 108,
			"formato" : "wav",
			"duracion" : 76,
			"inicio" : 0,
			"fin" : 76,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 85,
				"nombre_fuente": "Voces",
				"descripción": "Sonido de voces humanas en un restaurant.",
				"nombre_fuente_categoria": "Humanos"			
			}]
		}]

	},
	
	{ 
		"ID_archivo" : 10,
		"sonido": encode_audio("gato10.wav"),
		"formato" : "wav",
		"exterior" : "interior",
		"fecha_grabacion" : "27-06-2021",
		"duracion" : 25,
		"latitud" : -39.83628621780177,
		"longitud" : -73.21570963049898,
		"ciudad" : "Valdivia", 
		"fecha upload" : "27-06-2021",
		"Usuario" : {
			"RUT": "13276536-7",
			"nombre": "Jose",
			"apellido": "Tellez",
		},
		"Segmentos" : [{
			"ID_segmento" : 109,
			"formato" : "wav",
			"duracion" : 25,
			"inicio" : 0,
			"fin" : 25,
			"Analizar": [{
				"tipo_analizador" : "Maquina",
				"porcentaje" : 97,
				"nombre_fuente": "Gato",
				"descripción": "Sonido de ronroneo y maullido de gato.",
				"nombre_fuente_categoria": "Animales"			
			}]
		}]

	}
	
	
	])


AgegarDato(collection)

