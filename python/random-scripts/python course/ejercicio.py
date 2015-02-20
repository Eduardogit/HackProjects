#!/usr/bin/python
import os
try:
	opcion = int(raw_input(
		"BIENVENIDO AL SISTEMA ::HACK:: LOL"
		+"\n\n\n\n\n[1] SISTEMA OPERATIVO"
		+"\n\n\n\n\n[2] ESPACIO EN DISCO"
		+"\n\n\n\n\n[3] ARQUITECTURA\n>:"
		))

	print opcion

	if opcion == 1:
		print"ESTOY EN SISTEMA OPERATIVO"
		os.system('uname -a')
	elif opcion == 2:
		print"ESTOY EN ESPACIO DE DISCO"
		os.system('df -h')
	elif opcion == 3:
		print"ESTOY EN ARQUITECTURA"
		os.system('lshw -C CPU | grep width')
except KeyboardInterrupt:
	print "\rsaliendo.."