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
	   ]
search = ['1','2','3','4']
option = 0

def FILES():
	phrase = raw_input("\n\nTYPE THE FILE NAME THAT YOU LIKE TO FIND\n>:")
	for files in os.walk('/'):
		for filename in files:
			for search in filename:
				if "." in search:
					if phrase == search:
						location = sub.check_output("pwd")
						print "[+]FILE FOUND [%s]\n[+]LOCATION [%s]"%(search,location)
						break


def FOLDERS():
	for base, dirs, files in os.walk('/'):
		print base

def SPECIFICFILE():
	for base, dirs, files in os.walk('/'):
		print files


def SPECIFICWORD():
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
	FILES()

elif option == "2":
	FOLDERS()
elif option == "3":
	SPECIFICFILE()
elif option == "4":
	SPECIFICWORD()