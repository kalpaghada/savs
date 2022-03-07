import os
import json
from collections import Counter

detected_objects_path = "../imagedetection/detected_objects/"

for entry in os.scandir(detected_objects_path):
	#with open('detected_objects.txt') as f:
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	print(filename)
	with open(detected_objects_path+filename+'.objects') as f:
		counts = Counter()
		for line in f.readlines():
			counts.update(json.loads(line.replace("'", '"')))

	with open(os.getcwd()+'/condensed_objects/'+filename+'.condensed','w') as g:
		for fruit, count in counts.items():
			print(f"{fruit}:{count}")
			g.write(f"{fruit}:{count}"+'\n')

	f.close()
	g.close()
