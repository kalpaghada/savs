import os

os.system("python3 speechrecognition/main.py")

f = open("speechrecognition/output.txt","r")
lines = f.read()
f.close()

os.system("python3 videosearch/search.py "+'"{0}"'.format(lines))
