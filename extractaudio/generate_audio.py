#ffmpeg -i video.mp4 -f wav [-ab 192000] -vn audio.wav

import os

video_database_path = "../imagedetection/video_database"

for entry in os.scandir(video_database_path):
	print(entry.path)
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	os.system("ffmpeg -i "+"'{0}'".format(entry.path)+" -f wav -vn "+"audio_files/"+"'{0}'".format(filename)+".wav")
