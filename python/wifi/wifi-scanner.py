#!/usr/bin/env python
from wifi import Cell
from pcapy import *
import time
import os
wifi_list = []
tmp = []
ini  = [
"		                                                     \n",
"                -                                           \n",
"               //                                           \n",
"              //                                            \n",
"             / \                                            \n",
"            /   \  -                                        \n",
"           /    | /|                                        \n",
"          /     |/ |                                        \n",
"         /         /                                        \n",
"        /         /                                         \n",
"       /         /                                          \n",
"      /         /          _____                            \n",
"     /         /    ______/ ___ \_________     _            \n",
"    |         /    /      <----/          \___/ \           \n",
"     \       /     \__________/    _    _    _   \          \n",
"      \     /               \     \  \  \ \  \ \  \         \n",
"       \    \                \     \  \  \ \  \ \  \        \n",
"        \    \                \     \  \  \ \  \ \__\       \n",
"         \    \_              /    /    \  \ \__\           \n",
"          \_    \_           /   _/      \__\               \n",
"            \_    \_____  __/  _/                           \n",
"              \_________][____/                         ___ \n",
"  __  __   ___    __              ________     ____    /\__\ \n",
" /\_\-\_\-\___\  /\_\    ______  /\_______\   /\___\  / /  /\n",
" \/  \ \ \ \   \ \/  \  /\_____\ \/    _   \  \/    \/ /  / \n",
"  \   \_\ \_\   \ \   \ \/_____/  \   |_>  /   \     \/  /  \n",
"   \_____/\_____/  \__/            \    __/     \__     /   \n",
"                                    \   \  ___    /    /    \n",
"                                     \__/ /\__\  /    /     \n",
"                                         / /  /_/    /      \n",
"                                         \/         /       \n",
"                                          \________/        \n"        
"" 
       ]
try:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = "\033[1m"

	def disable():
	    HEADER = ''
	    OKBLUE = ''
	    OKGREEN = ''
	    WARNING = ''
	    FAIL = ''
	    ENDC = ''

	def OK( msg):
	    print BOLD + msg + ENDC

	def info( msg):
	    print OKBLUE + msg + ENDC

	def warning( msg):
	    print WARNING + msg + ENDC

	def important( msg):
    print FAIL + msg + ENDC

	def dispositivos():
		devs = findalldevs()
		print "[+]Selecciona un Dispositivo"
		for cont,i in enumerate(devs):
			if "wlan" in i:
				OK("\v[%i]  %s"%(cont,i))
		seleccion = int(raw_input("\n\n[+] Elige uno\n >:"))
		return devs[seleccion]

	def escaneo(x):
		objeto = Cell.all(x)
		return objeto


	def nuevaRed(x):
		wifi_list.append(x)
		return wifi_list

	def archivo(x):
		os.system('touch wifi_list.txt')
		f = open("wifi_list.txt","w")
		for item in x:
		    f.write(str(item.ssid) + "\n")

		f.close()


	for i in ini:
		important( i.rstrip())
		time.sleep(.09)
	disp = dispositivos()
	info (
			    "------------------------------------------------------\n\n"
				"\tE S C A N E A N D O   C O N : %s \n\n"
				"------------------------------------------------------\n\n"%disp
				)
	while True:
		cell = escaneo(disp)
		os.system('clear')		
		print cell
		if tmp == []:
			tmp = len(cell)
			wifi_list = cell
		if len(cell) > tmp:
			wifi_list=nuevaRed(cell[-1])
			tmp = len(cell)		
			print "UNA RED NUEVA"+str(tmp)
		elif len(cell)==tmp:
			tmp = len(cell)
			print "NINGUNA RED NUEVA"+str(tmp)
		elif len(cell)<tmp:
			wifi_list=nuevaRed(cell[-1])
			tmp = len(cell)
			print "UNA RED MENOS "+str(tmp)
		print "[#]      BSSID               PWR   QUALITY    CHANNEL  ENCRYPTATION  ESSID\n\n"
		for cont,i in enumerate(wifi_list):			
				print "[+]%i     %s    %s    %s        %s        %s       %s"%(cont,i.address,i.signal,i.quality,i.channel,i.encryption_type,i.ssid)
			
except KeyboardInterrupt, e:
	important (
					  "\b \t\t\t ----------------------------------\n"
					  "\t\t\tP R O G R A M A  F I N A L I Z A D O\n\n"
					  "[+]Redes encontradas %i\n[+]SSID "%len(wifi_list)
					)
	for i in wifi_list:
		print "[+]%s"%i.ssid
	print("Redes volcadas en el archivo wifi_list.txt")
	archivo(wifi_list)
	#INSTALE AIRCRACK
	#instale libssl-dev
