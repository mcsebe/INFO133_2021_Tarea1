import folium
import branca
import webbrowser
from pymongo import MongoClient
from add_wavfile import decode_audio
from playsound import playsound

mapa = folium.Map(location = [-39.81730435463257, -73.24257650930436], zoom_start=13 ,control_scale = True)


def MostrarDia(mapa):
	MONGO_URI = 'mongodb://localhost'

	client = MongoClient(MONGO_URI)

	db = client['Tarea']
	collection = db['Audios']
	

	for documento in collection.find():
		html = "<p>ID: " + str(documento['ID_archivo']) + " </p>"
		html += "<p>Latitud: " + str(documento['latitud']) + " </p>"
		html += "<p>Longitud: " + str(documento['longitud']) + "</p>"
		html += "<p>Duracion : " + str(documento['duracion']) + "s</p>"
		html += "<p>Formato: " + str(documento['formato']) + "</p>"
		html += "<p>Exterior: " + str(documento['exterior']) + "</p>"
		html += "<p>Fecha de grabacion: " + str(documento['fecha_grabacion']) + "</p>"
		html += "<p>Nombre de la fuente: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente']) + "</p>"
		html += "<p>Categoria: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) + "</p>"
			
		iframe3 = branca.element.IFrame(html=html, width=800, height=340)
	
		marcador1 = folium.Marker(location= [documento['latitud'], documento['longitud']],
			popup = folium.Popup(iframe3, max_width=340),
			icon = folium.Icon(color="black")
		)
		marcador1.add_to(mapa)
		
MostrarDia(mapa)

mapa.save("mapa_test.html")
webbrowser.open("mapa_test.html")


#############


from tkinter import *
from tkinter import messagebox as MessageBox

def send_data():
	mapa = folium.Map(location = [-39.81730435463257, -73.24257650930436], zoom_start=13 ,control_scale = True)

	MONGO_URI = 'mongodb://localhost'

	client = MongoClient(MONGO_URI)

	db = client['Tarea']
	collection = db['Audios']
	
	fechavalor_info = fechavalor.get()
	Humanos_info = bool(Humanos.get())
	Musica_info = bool(Musica.get())
	Animales_info = bool(Animales.get())
	Ambientales_info = bool(Ambientales.get())
	Mecanicos_info = bool(Mecanicos.get())
	Vehiculos_info = bool(Vehiculos.get())
	Alertas_info = bool(Alertas.get())
    	
	if (fechavalor_info != "" and fechavalor_info != "-"):
		for documento in collection.find({ "fecha_grabacion": fechavalor_info}):

			cond1 = (Humanos_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Humanos")
			cond2 = (Musica_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Musica")
			cond3 = (Animales_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Animales")
			cond4 = (Ambientales_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Climáticos y Medio ambientales")
			cond5 = (Mecanicos_info and (str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Mecanico"))
			cond6 = (Vehiculos_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Vehiculos")
			cond7 = (Alertas_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Alertas")
			
			if (cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7):
				html = "<p>ID: " + str(documento['ID_archivo']) + " </p>"
				html += "<p>Latitud: " + str(documento['latitud']) + " </p>"
				html += "<p>Longitud: " + str(documento['longitud']) + "</p>"
				html += "<p>Duracion : " + str(documento['duracion']) + "s</p>"
				html += "<p>Formato: " + str(documento['formato']) + "</p>"
				html += "<p>Exterior: " + str(documento['exterior']) + "</p>"
				html += "<p>Fecha de grabacion: " + str(documento['fecha_grabacion']) + "</p>"
				html += "<p>Nombre de la fuente: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente']) + "</p>"
				html += "<p>Categoria: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) + "</p>"

				iframe3 = branca.element.IFrame(html=html, width=800, height=340)
			
				marcador1 = folium.Marker(location= [documento['latitud'], documento['longitud']],
					popup = folium.Popup(iframe3, max_width=340),
					icon = folium.Icon(color="black")
				)
				marcador1.add_to(mapa)
	else:
		for documento in collection.find():

			cond1 = (Humanos_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Humanos")
			cond2 = (Musica_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Musica")
			cond3 = (Animales_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Animales")
			cond4 = (Ambientales_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Climáticos y Medio ambientales")
			cond5 = (Mecanicos_info and (str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Mecanico"))
			cond6 = (Vehiculos_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Vehiculos")
			cond7 = (Alertas_info and str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) == "Alertas")
			

			if (cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7):

				html = "<p>ID: " + str(documento['ID_archivo']) + " </p>"
				html += "<p>Latitud: " + str(documento['latitud']) + " </p>"
				html += "<p>Longitud: " + str(documento['longitud']) + "</p>"
				html += "<p>Duracion : " + str(documento['duracion']) + "s</p>"
				html += "<p>Formato: " + str(documento['formato']) + "</p>"
				html += "<p>Exterior: " + str(documento['exterior']) + "</p>"
				html += "<p>Fecha de grabacion: " + str(documento['fecha_grabacion']) + "</p>"
				html += "<p>Nombre de la fuente: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente']) + "</p>"
				html += "<p>Categoria: " + str(documento['Segmentos'][0]['Analizar'][0]['nombre_fuente_categoria']) + "</p>"

				iframe3 = branca.element.IFrame(html=html, width=800, height=300)
			
				marcador1 = folium.Marker(location= [documento['latitud'], documento['longitud']],
					popup = folium.Popup(iframe3, max_width=300),
					icon = folium.Icon(color="black")
				)
				marcador1.add_to(mapa)
				
    
	mapa.save("mapa_test.html")
	webbrowser.open("mapa_test.html")



def play():
	ID_info = int(ID.get())
	
	MONGO_URI = 'mongodb://localhost'

	client = MongoClient(MONGO_URI)

	db = client['Tarea']
	collection = db['Audios']
	info = collection.find({ "ID_archivo": ID_info})[0]
	
	decode_audio(info["sonido"])

# Create new instance - Class Tk()
mywindow = Tk()
mywindow.geometry("450x500")
mywindow.title("Mapa de Audios en Valdivia")
mywindow.resizable(False, False)
mywindow.config(background="#F8F7EF")
main_title = Label(text="Bienvenido \nLlene los datos que desea filtrar y aprete siguiente", font=(
    "Arial", 14), bg="#A2BAB9", fg="black", width="500", height="2")
main_title.pack()

opciones1 = ["-","25-06-2021","26-06-2021","27-06-2021","28-06-2021","29-06-2021","30-06-2021"]

# Define Label Fields
fecha_label = Label(
    text="Seleccione la Fecha: ", bg="#F8F7EF", font=("Arial", 12))
fecha_label.place(x=150, y=70)


estadoFinal_label = Label(
    text="Seleccione la categoria: ", bg="#F8F7EF", font=("Arial", 12))
estadoFinal_label.place(x=150, y=150)


fechavalor = StringVar()
fecha = OptionMenu(mywindow, fechavalor,*opciones1)
fecha.config(width=10)
fecha.place(x=150, y=105)

Humanos = IntVar()
Checkbutton(mywindow, text="Humanos", variable=Humanos, bg="#F8F7EF").place(x=50, y=180)
Musica = IntVar()
Checkbutton(mywindow, text="Música", variable=Musica, bg="#F8F7EF").place(x=50, y=210)
Animales = IntVar()
Checkbutton(mywindow, text="Animales", variable=Animales, bg="#F8F7EF").place(x=50, y=240)
Ambientales = IntVar()
Checkbutton(mywindow, text="Climáticos y Medio ambientales", variable=Ambientales, bg="#F8F7EF").place(x=50, y=270)
Mecanicos = IntVar()
Checkbutton(mywindow, text="Mecanicos", variable=Mecanicos, bg="#F8F7EF").place(x=300, y=180)
Vehiculos = IntVar()
Checkbutton(mywindow, text="Vehiculos", variable=Vehiculos, bg="#F8F7EF").place(x=300, y=210)
Alertas = IntVar()
Checkbutton(mywindow, text="Alertas", variable=Alertas, bg="#F8F7EF").place(x=300, y=240)



# Submit Button
siguiente_btn = Button(mywindow, text="Siguiente", width="30",
                       height="2", command=send_data, bg="#A2BAB9")
siguiente_btn.place(x=100, y=310)

fecha_label = Label(
    text="Ingrese la ID del audio\nque desea reproducir :", bg="#F8F7EF", font=("Arial", 12))
fecha_label.place(x=150, y=370)
# Get and store data from users
ID = StringVar()
ID_entry = Entry(textvariable=ID, width="10")
ID_entry.place(x=150, y=420)

play_button = Button(mywindow, text="Play", font=("Helvetica", 12), command=play)
play_button.place(x=250, y=420)


mywindow.mainloop()
