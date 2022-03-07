import os
import sys
from itertools import chain

condensed_objects_path = "../../imagedetection/condensed_objects/"
#List of all hit_path temporary sets for every hit
storage_list = []
temp_list = []

#MAIN
for i in range(1, len(sys.argv)):
#
	temp_list = []
	#print("set cleared: "+str(temp_list))
	
	count = 0
	hit_path = ""
	
	for entry in os.scandir(condensed_objects_path):
	#	
		f = open(entry.path, "r")
		lines = f.readlines()
		f.close()
		
		for line in lines:
		#
			line = line.split(':')
			if line[0] == sys.argv[i]:
				hit_path = entry.path
				count = int(line[1])
				#print("###HIT### = "+hit_path+", count = "+str(count))
				temp_list.append(hit_path)
				#print("\t "+str(temp_list))
				break
		#		
	#
	
	storage_list.append(temp_list)
	#print("STORAGE_LIST after an argument: "+str(storage_list))
	print("Results for "+sys.argv[i]+":")
	print(str(temp_list))
	print()

#

result = []

result = list(chain.from_iterable(storage_list))
#result = set(storage_list[i])

print("Result for", " & ".join([str(sys.argv[i]) for i in range(1, len(sys.argv))]), ":")
for i in storage_list: #range(1, len(sys.argv)):
	result = (set(result) & set(i))
print(result)

#print("storage list:")
#for i in storage_list:
#	print(i)
