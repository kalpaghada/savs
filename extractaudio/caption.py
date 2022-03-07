import os
import speech_recognition as sr

r = sr.Recognizer()

audio_files_path = "audio_files"

for entry in os.scandir(audio_files_path):
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	
	inp = sr.AudioFile('audio_files/'+filename+'.wav')
	with inp as source:
		audio = r.record(source)

	#main
	text = r.recognize_sphinx(audio)
	print(text)
	f = open("captions/"+filename+".caption","w")
	f.write(text)
	f.close()
