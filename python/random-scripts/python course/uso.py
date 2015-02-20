#!/usr/bin/python 
import os 
usage_sys = [
				"\nmodo de empleo: chmod +x [\'ARCHIVO\']\n"
				"ejecucion: ./[\'ARCHIVO\']  \n" 
				"\t-n,  nombre de el sistema\n"
				"\t-p,      ip de la maquina\n"
				"\t-m,   marca de la maquina\n"
			]
for i  in usage_sys: 
	print i

print "\n\n\n\n\n B I E N V E N I D O            d\n\n\n\n\n\n"

print "NOMBRE EQUIPO   "+str(os.system('uname -a'))
print "IP              "+str(os.system('hostname -i'))
print "MARCA DE LA COMP"+str(os.system('dmidecode -s system-manufacturer'))
			
