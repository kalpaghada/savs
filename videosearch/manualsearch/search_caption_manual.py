import os
import sys
from itertools import chain

video_captions_path = "../../extractaudio/captions/"
video_database_path = "../../imagedetection/video_database/"
storage_list = []
temp_list = []

for i in range(1,len(sys.argv)):
	
	temp_list = []

	for entry in os.scandir(video_captions_path):
		
		f = open(entry.path, "r")
		lines = f.read()
		f.close()
		
		filename = os.path.splitext(os.path.basename((entry.path)))[0]
		
		if (sys.argv[i] in lines):
			temp_list.append(entry.path)
			continue
	
	storage_list.append(temp_list)
	print("Results for "+sys.argv[i]+":")
	print(str(temp_list))
	print()

result = []

result = list(chain.from_iterable(storage_list))

print("Result for", " & ".join([str(sys.argv[i]) for i in range(1, len(sys.argv))]), ":")
for i in storage_list:
	result = (set(result) & set(i))
print(result)
