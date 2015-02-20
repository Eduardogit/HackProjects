


mi_lista = [1,2,3,4,5,6,7,8,9]

f = open("salida.txt", "w")

for item in mi_lista:
	print"Volcando en archivo"+str(item)
	f.write(str(item) + "\n")

f = open("salida.txt", "r")

for item in f:
	print item






f.close()