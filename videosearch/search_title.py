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

video_database_path = "../imagedetection/video_database/"

hit_path = ""
box = []
y = 100

for entry in os.scandir(video_database_path):
	
	box = []
	found = 0
	
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
		
	for i in range(1,len(sys.argv)):
		count = 0
		
		for word in filename.lower().split():
			if (sys.argv[i] == word):
				count += 1
				continue
		
		if (count != 0):
			found += 1
			
		box.append(count)
		
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
			hit_path = video_database_path + str(filename) + ".mp4"
		#else if (F(box) == y):
				

if (hit_path != ""):
	print(hit_path)
	os.system("parole "+"'{0}'".format(hit_path)) #enter your video player command here.
else:
	print("No matches found.")
