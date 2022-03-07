import os
import sys
#Separate subject and object. From object, extract everything (verbs and nouns) except things like - a, to, with, on...
import spacy
nlp = spacy.load('en_core_web_sm')
spacy_doc = nlp(sys.argv[1])

print("INPUT: "+str(spacy_doc))

x = 2 #search for objects by default if not explicitly mentioned.
processed_text = ""

spacy_subject = ""
for text in spacy_doc:
	if (text.pos_ != "ADP") & (text.pos_ != "ADV") & (text.pos_ != "DET") & (text.pos_ != "CCONJ") & (text.pos_ != "PRON"):
		spacy_subject = text.orth_
		if (spacy_subject != "video") & (spacy_subject != "search") & (text.lemma_ != "contain") & (spacy_subject != "has") & (text.lemma_ != "be"):
			if (text.lemma_ == "title"):
				x = 1
				continue
			if (text.lemma_ == "caption") | (text.lemma_ == "talk"):
				x = 3
				continue
			processed_text += spacy_subject.lower() + " "

if (x == 1):
	print("searching by TITLE...\n")
	#title = str(input())
	#os.system("python3 search_title.py "+ title)
	os.system("python3 videosearch/search_title.py " + processed_text) # the directory is because it's being called by run.py which is in the main directory - all directories have to be wrt run.py
if (x == 2):
	
	# imageai specific preprocessing
	
	processed_text = nlp(processed_text)
	processed_text = " ".join([token.lemma_ for token in processed_text])
	
	if ("tennis" in processed_text): # Fixing input to comply with ImageAI's detection classes. Remove if not using ImageAI.
		processed_text = processed_text.replace("tennis","'{0}'".format("tennis racket"))
		
	if ("football" in processed_text):
		processed_text = processed_text.replace("football","'{0}'".format("sports ball"))
	if ("basketball" in processed_text):
		processed_text = processed_text.replace("basketball","'{0}'".format("sports ball"))
	if ("baseball" in processed_text):
		processed_text = processed_text.replace("baseball","'{0}'".format("sports ball"))
		
	if ("wine" in processed_text):
		processed_text = processed_text.replace("wine","'{0}'".format("wine glass"))
		
	if ("dining table" in processed_text):
		processed_text = processed_text.replace("dining table","'{0}'".format("dining table"))
	elif ("table" in processed_text):
		processed_text = processed_text.replace("table","'{0}'".format("dining table"))
	
	if ("hair dryer" in processed_text):
		processed_text = processed_text.replace("hair dryer","'{0}'".format("hair dryer"))
		
	if ("hot dog" in processed_text):
		processed_text = processed_text.replace("hot dog","'{0}'".format("dog"))
		
	if ("fire hydrant" in processed_text):
		processed_text = processed_text.replace("fire hydrant","'{0}'".format("fire hydrant"))
	
	if ("stop sign" in processed_text):
		processed_text = processed_text.replace("stop sign","'{0}'".format("stop_sign"))
		
	if ("parking meter" in processed_text):
		processed_text = processed_text.replace("parking meter","'{0}'".format("parking meter"))
		
	if ("traffic light" in processed_text):
		processed_text = processed_text.replace("traffic light","'{0}'".format("traffic light"))
	
	print("searching by CONTENT...\n")
	#content = str(input())
	#os.system("python3 search_content.py "+ content)
	os.system("python3 videosearch/search_content.py " + processed_text)
if (x == 3):
	print("searching by CAPTIONS...\n")
	#caption = str(input())
	#os.system("python3 search_caption.py "+ caption)
	os.system("python3 videosearch/search_caption.py " + processed_text)
		
