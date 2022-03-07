import os
import sys
from itertools import chain
import statistics
import math

def F(X):
    if (len(X) == 1):
        return (1/X[0])
		
    sd = statistics.stdev(X)
    mean = statistics.mean(X)
    return ((sd/math.pow(mean,len(X)-1)) + (1/math.pow(mean,1)))

condensed_objects_path = "../imagedetection/condensed_objects/"
video_database_path = "../imagedetection/video_database/"

hit_path = ""

box = []
y = 100

#MAIN
for entry in os.scandir(condensed_objects_path):
	
	box = []
	found = 0
	count = 0
	
	f = open(entry.path, "r")
	lines = f.readlines()
	f.close()
	
	for i in range(1, len(sys.argv)):
		
		for line in lines:
			
			line = line.split(':')
			
			if line[0] == sys.argv[i]:
				count = int(line[1])
				box.append(count)
				found += 1
				break
	
	if (found != (len(sys.argv)-1)):
		for j in range(0, len(sys.argv) - 1 - found):
			box.append(0)
	
	zero = True
	for number in box:
		if (number != 0):
			zero = False
			break
	if (zero == True):
		continue
	else:
		print(str(box) + str(F(box)))
		if (F(box) < y):
			y = F(box)
			hit_path = video_database_path+os.path.splitext(os.path.basename((entry.path)))[0]+".mp4"

if (hit_path != ""):
	print(hit_path)
	os.system("parole "+"'{0}'".format(hit_path)) #enter your video player command here.
else:
	print("No matches found.")
