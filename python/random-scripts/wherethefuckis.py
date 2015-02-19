#!/usr/bin/env python
# -*- coding: utf-8 -*-
import color
import os
from time import sleep
import subprocess as sub
os.system('clear')
images   = [".gif",".png",".jpg",".jpeg",".svg"]
document = [".doc",".pdf",".xls",".xml",".txt"]
code     = [".html",".js",".sh",".c",".h",".py",".rb",".java",".class"]
audio    = [".mp4",".mp3",".wav",".wma",".ogg"]
menu     = [
		"\t====================[ WFF ] =====================",
		"\t=== [W] H E R E the [F] U C K is my [F] I L E ===",
		"\t=================================================",
		"\t      [       Select the target          ]\n\n\n ",
		"[1] FILES     					     				",
		"[2] FOLDERS 						  				",
		"[3] SPECIFIC FILES 				      			",
		"[4] SPECIFIC WORD 					  				",
		"[5] EXTRAS PASSWORDS,LOGS,ETC 		  				"
	   ]
search   = ['1','2','3','4']
option   = 0
minidb   = []
def FILES(phrase):
	TotalFiles = 0
	try:
		phrase = phrase.lower()
		for base,dirs, files in os.walk('/'):
			for filerow in files:
				filerow = filerow.lower()
				if phrase in filerow:
					color.infog("[+]FILE FOUND [%s]=>[%s]"%(filerow,base))
					TotalFiles += 1
		print "TOTAL FILES FOUND [ %i ]"%TotalFiles
	except Exception, e:
		raise e
###############
### xdg-open [URL]
###############
def FOLDERS(phrase):
	try:
		phrase = phrase.lower()
		for base, dirs, files in os.walk('/'):
			dirs = map(lambda x: x.lower(), dirs)
			for singledir in dirs:
				if phrase == singledir:
					color.infog("[+]FILE FOUND [%s]=>[%s]"%(singledir,base))
	except Exception, e:
		raise e
	

def SPECIFICFILES():
	os.system('clear')
	color.warn("====[    S P E C I F I C  F I L E     ]===")
	print "CHOOSE FILE TYPE"
	file_type = raw_input("\n[1] images\n[2] document\n[3] code\n[4] audio\n\n\n>:")
	########################### [ IMAGES  ] ###########################
	if file_type   == "1":
		for number,i in enumerate(images):
			print "[%i] %s"%(number+1,i)
		choose = input("\n>:")
		for base,dirs,files in os.walk('/home/desktopadmin/Imágenes'):
			for single in files:
				if single.endswith(images[choose-1]):
					color.infog( "FILE FOUND[%s]=>[%s]"%(single,base))

	########################### [ DOCUMENTS  ] ###########################
	elif file_type == "2":
		for number,i in enumerate(document):
			print "[%i] %s"%(number+1,i)
		choose = input("\n>:")
		for base,dirs,files in os.walk('/'):
			for single in files:
				if single.endswith(document[choose-1]):
					color.infog( "FILE FOUND[%s]=>[%s]"%(single,base))
	########################### [ CODE  ] ###########################
	elif file_type == "3":
		for number,i in enumerate(code):
			print "[%i] %s"%(number+1,i)
		choose = input("\n>:")
		for base,dirs,files in os.walk('/'):
			for single in files:
				if single.endswith(code[choose-1]):
					color.infog( "FILE FOUND[%s]=>[%s]"%(single,base))
	########################### [ AUDIO  ] ###########################
	elif file_type == "4":
		for number,i in enumerate(audio):
			print "[%i] %s"%(number+1,i)
		choose = input("\n>:")
		for base,dirs,files in os.walk('/'):
			for single in files:
				if singlengle.endswith(audio[choose-1]):
					color.infog( "FILE FOUND[%s]=>[%s]"%(single,base))




def SPECIFICWORD(phrase):
	for base, dirs, files in os.walk('/'):
		print files






###### SHOW THE TITLE ###########
for menu_line in menu:
	if "[5] EXTRAS PASSWORDS,LOGS,ETC" in menu_line:
		color.info(menu_line)
	else:
		color.err(menu_line)
		

##### VALIDATING OPTIONS ########
while option not in search:
	option = raw_input("SELECT OPTION \n>:")
	if option not in search:
		color.info ("TYPE THE OPTION NUMBER")

### SELECTING OPTION #########
if option   == "1":
	os.system('clear')
	color.warn("======[    F I L E S         ]=====")
	phrase = raw_input("FILE NAME \n>:")
	FILES( phrase )
elif option == "2":
	os.system('clear')
	color.warn("======[    F O L D E R S     ]=====")
	phrase = raw_input("FOLDER NAME \n>:")
	FOLDERS(phrase)
elif option == "3":
	SPECIFICFILES()
elif option == "4":
	os.system('clear')
	color.warn("=====[    S P E C I F I C   W O R D   ]====")
	phrase = raw_input("WORD \n>:")
	SPECIFICWORD(phrase)


#############
##TO-DO LIST
###LINK THAT OPEN THE CURRENT FOLDER IN ALL THE FUNCTIONS
###SPECIFIC FILES THEN LIST ALL THE EXTENSION FILES SEARCH ONE SPECIFIC
###DO THE FINAL MENU PASSWORDS LOGS ETC
###
###
###
###
###
###