from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import matplotlib

execution_path = os.getcwd()

#Prints object details every frame
def forFrame(frame_number, output_array, output_count):
	print("FOR FRAME ",frame_number)
	print("Output for each object: ",output_array)
	print("Output count for unique objects: ",output_count)
	f.write(str(output_count)+"\n")
	print("----------------END OF A FRAME---------------")
	f.flush()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

#__MAIN__

video_database_path = "../imagedetection/video_database"

for entry in os.scandir(video_database_path):
	print(entry.path)
	filename = os.path.splitext(os.path.basename((entry.path)))[0]
	f = open(execution_path+"/detected_objects/"+filename+".objects","a")
	video_path = detector.detectObjectsFromVideo(input_file_path = os.path.join(execution_path, "video_database/"+filename+".mp4"), output_file_path = os.path.join(execution_path, "processed_videos/"+filename), frames_per_second = 20, log_progress = True, per_frame_function = forFrame)
	print(video_path)
	f.close()
