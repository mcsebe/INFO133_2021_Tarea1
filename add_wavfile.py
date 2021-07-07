import base64
from playsound import playsound
from os import remove


def encode_audio(direccion):
	audio = open("./Audio/" + direccion, "rb")
	audio_content = audio.read()
	return base64.b64encode(audio_content)
  
def decode_audio(codigo):
	info = base64.b64decode(codigo)
	with open('myfile.wav', mode='bx') as f:
		f.write(info)

	playsound("myfile.wav")
	remove('myfile.wav')

