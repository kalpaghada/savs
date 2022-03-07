import speech_recognition

r = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

def record():
	global audio
	try:
		with mic as source:
			audio = r.listen(source)
	except:
		print("couldn't recognize audio")
		record()

def recognize():
	try:
		#recognize_sphinx(audio)
		text = r.recognize_sphinx(audio)
		print(text)
		#f = open("output.txt","w")
		f = open("speechrecognition/output.txt","w") # for run.py
		f.write(text)
		f.close()
	except:
		print("couldn't recognize audio")

#main

while True:
	print("record?")
	x = int(input())
	if (x == 1):
		print("speak:")
		record()
		print("recognizing:")
		recognize()
	else:
		break
