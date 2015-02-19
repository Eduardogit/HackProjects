import os
from time import sleep
import subprocess as sub
os.system('clear')
menu = [
		"\t====================[ FSS ] ===================\n"
		"\t=== [F] i l e [S] e a r c h [S] c a n n e r ===\n"
		"\t===============================================\n"
		"\t      [       Select the target          ]\n\n\n"
		"[1] FILES     					      \n"
		"[2] FOLDERS 						  \n"
		"[3] SPECIFIC FILE 				      \n"
		"[4] SPECIFIC WORD 					  \n"
		"[5] EXTRAS PASSWORDS,LOGS,ETC 		  \n"
	   ]
search   = ['1','2','3','4']
option   = 0
def FILES(phrase):
	TotalFiles = 0
	try:
		phrase = phrase.lower()
		for base,dirs, files in os.walk('/'):
			for filerow in files:
				filerow = filerow.lower()
				if phrase in filerow:
					print "[+]FILE FOUND [%s]=>[%s]"%(filerow,base)
					TotalFiles += 1
		print "TOTAL FILES FOUND [ %i ]"%TotalFiles
	except Exception, e:
		raise e
	
def FOLDERS(phrase):
	try:
		phrase = phrase.lower()
		for base, dirs, files in os.walk('/'):
			dirs = map(lambda x: x.lower(), dirs)
			for singledir in dirs:
				if phrase == singledir:
					print "[+]FILE FOUND [%s]=>[%s]"%(singledir,base)
			sleep(2)
	except Exception, e:
		raise e
	

def SPECIFICFILE(ext,phrase):
	for base, dirs, files in os.walk('/'):
		print files


def SPECIFICWORD(phrase):
	for base, dirs, files in os.walk('/'):
		print files






###### SHOW THE TITLE ###########
for menu_line in menu:
	print menu_line

##### VALIDATING OPTIONS ########
while option not in search:
	option = raw_input("SELECT OPTION \n>:")
	if option not in search:
		print "\nTYPE THE OPTION NUMBER\n"

### SELECTING OPTION #########
if option   == "1":
	phrase = raw_input("FILE NAME \n>:")
	FILES( phrase )
elif option == "2":
	phrase = raw_input("FOLDER NAME \n>:")
	FOLDERS(phrase)
elif option == "3":
	ext = raw_input("EXTENTION FILE  \n>:")
	phrase = raw_input("FILE NAME\n")
	SPECIFICFILE(ext,phrase)
elif option == "4":
	phrase = raw_input("WORD \n>:")
	SPECIFICWORD(phrase)