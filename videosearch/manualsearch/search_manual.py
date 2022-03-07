import os
import sys

print("SEARCHING FOR: "+sys.argv[1])

print("1. search by title")
print("2. search by content")
print("3. search by captions")
x = int(input())
if (x == 1):
	#title = str(input())
	#os.system("python3 search_title.py "+ title)
	os.system("python3 videosearch/search_title_manual.py " + sys.argv[1]) #Because it's being called by run.py which is in the main directory
if (x == 2):
	#content = str(input())
	#os.system("python3 search_content.py "+ content)
	os.system("python3 videosearch/search_content_manual.py " + sys.argv[1])
if (x == 3):
	#caption = str(input())
	#os.system("python3 search_caption.py "+ caption)
	os.system("python3 videosearch/search_caption_manual.py " + sys.argv[1])
		
