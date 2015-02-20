#!/usr/bin/python
print "\n\n\t\tSecuencias de escape \n\n"
time.sleep(1.2)
usage_escape =[  
			      "\n  <-- nueva linea        \n"
				  +"\\  <--Barra invertida     \n"
				  +"\'  <--Comilla simple      \n"
				  +"\"  <--Comilla doble       \n"
				  +"\a  <--Campanilla            "
				  +"\b  <--Retroceso           \n"
				  +"\f  <--Nueva pagina        \n"
				  +"DELETE ME                    "
				  +"\r  <--Retorno de carro    \n"
				  +"\t  <--Tabulador horizontal\n"
				  +"tabulando verticalmente ...  "
				  +"\v\v <--Tabulador vertical \n"
				  +"\064<-- CARACTER ASCII     \n"
				  +"\x45<-- caracter ASCI con codigo hexadecimal hh " 
	          ]

for i in usage_escape:
	print i


print "\n\n\t\tImprimiendo tipos de datoss\n\n"
chain   = "Mi string"
integer = 5
Flot    = 5.5
print "%s STRING"      %chain
print "%i ENTERO"      %integer
print "%d ENTERO"      %integer
print "%o ENTERO Octal"%integer
print "%f Flotante    "%Flot



lista       = ['Lunes','Martes','Miercoles','Jueves', 'Viernes','Sabado','Domingo']
lista.sort()
lista.insert(0,"principio")
lista.append("final")
lista.index('lunes')
lista.remove("principio")
lista.reverse()
lista.count("Lunes")

tupla       = (1,2,3,4,5)
tupla[1:3]
#TUPLAS NO SOPORTAN ASIGNAR VALOR
tupla[1]=9
diccionario = {'Key','value':'key2','value2':'key3','value3'}
diccionario.has_key("something")
diccionario.keys()


#ENTRADA Y SALIDA



#CONDICIONAL
if :
	print "condicion normal"
#INSTRUCCION VACIA
if :

elif:
	pass
elif:

if :
elif:
else:

#tipos de condicionales

#BUCLES
rango_uno = range(8)

print rango_uno

rango_dos = range(1,8)


while rango_uno:
	pass
lista = ['uno','dos','tres']

for i in lista:
	print i 
a = "hola"
for pos, c in enumerate(a)
	print pos,c
#enumerar



#FUNCIONES