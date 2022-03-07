import os

p = "/speech-aided-video-search-master/imagedetection/video_database"

for entry in os.scandir(p):
	print(entry.path)
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	#base = os.path.basename(entry.path)
	#filename = os.path.splitext(base)[0]
	print(filename)
