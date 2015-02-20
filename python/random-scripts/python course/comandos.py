#!/user/bin/python
import os #echo hola 
import time as t 
command = []

def comandoEjecutar(x):
	if x == '':
		print "saliendo..."
		return 
	else:
		print "Realizando comando...\n\n"
		t.sleep(.5)
		print "RESULTADOS:"
		t.sleep(.5)
		os.system(x)
	
while command != '': 
	command = raw_input("Teclea un comando\n\n>:")
	comandoEjecutar(command)
