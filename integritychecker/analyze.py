import os
import sys
from itertools import chain
import statistics
import math
import spacy
nlp = spacy.load('en_core_web_sm')

def F(X):
	if (len(X) == 1):
		return (1/X[0])
		
	sd = statistics.stdev(X)
	mean = statistics.mean(X)
	return ((sd/math.pow(mean,len(X)-1)) + (1/math.pow(mean,1)))

video_database_path = "../imagedetection/video_database/"
video_captions_path = "../extractaudio/captions/"
condensed_objects_path = "../imagedetection/condensed_objects/"

box = []
integrity_box = dict()
y = 100

for entry in os.scandir(video_database_path):
	
	box = []
	found = 0
	
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	#print(filename)
	
	spacy_doc = nlp(filename.lower())
	filename_lemma = " ".join([token.lemma_ for token in spacy_doc])
	
	#print(filename_lemma)

	count = 0
		
	for word in filename_lemma.split(): # Fixing inputs to comply with ImageAI's detection classes. Remove if not using ImageAI.

		if word == "football":
			word = "sports ball"
		if word == "baseball":
			word = "sports ball"
		if word == "basketball":
			word = "sports ball"
		if word == "tennis":
			word = "tennis racket"
		if word == "table":
			word = "dining table"
		if word == "wine":
			word = "wine glass"
		if word == "kitten":
			word = "cat"
		if word == "puppy":
			word = "dog"
		if word == "hydrant":
			word = "fire hydrant"
		if word == "stop":
			word = "stop sign"
		if word == "parking":
			word = "parking meter"
		if word == "light":
			word = "traffic light"
		#fill this in.
		
		f = open(condensed_objects_path + str(filename) + ".condensed", "r")
		lines = f.readlines()
		f.close()
		
		temp = 0
		for line in lines:
			line = line.split(":")
			temp += int(line[1])
		
		for line in lines:
			line = line.split(":")
			if (line[0] == word):
				count = int(line[1])
				#print(line[0] + ": "+str(count))
				box.append((count/temp)*100)
				found += 1
				break
				
		count = 0
				
		f = open(video_captions_path + str(filename) + ".caption", "r")
		lines = f.read().split()
		f.close()
		
		temp = 0
		for line in lines:
			temp += 1
		
		for line in lines:
			
			if (line == word):
				count += 1
				found += 1
				continue
		
		if (count != 0):
			#print(word + ": "+str(count))
			box.append((count/temp)*100)
		
	#print(box)
	
	if (len(box) < 1):
		integrity_box[entry.path] = -1
		continue
	
	if (F(box) > F([1 for i in range(0,len(box))])):
		#print("SCORE: "+str(F(box))+entry.path + " - POSSIBLY SCAM.")
		integrity_box[entry.path] = F(box)
		
print("Videos that failed integrity check and are possibly deceptive:\n")
print("NEED IMMEDIATE ATTENTION:")
for i in integrity_box:
	if (integrity_box[i] == -1 ):
		print(str(i) + ", ("+str(integrity_box[i])+")"+"\n")

print("OTHER VIDEOS:")
for i in integrity_box:
	if (integrity_box[i] != -1 ):
		print(str(i) + ", "+"("+str(integrity_box[i])+")"+"\n")
