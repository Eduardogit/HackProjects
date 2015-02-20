total = [ 1, 2, 3, 5, 5, 5]
iguales=""
print "NUMERO DE ESPACIOS"
print len(total)
print "NUMEROS"
for i in total:
	 print total[i-1]
	 if total[i] == total[i-1]:
	 	iguales +=str(total[i])

print "NUMEROS IGUALES" + str(len(iguales))