import commands
import os
import subprocess as sub
cont     = 0
dev_list = []
def getIP():
    return commands.getoutput("hostname -I")


def scan():
    return sub.Popen(('sudo', 'nmap', '-sP', '192.168.1.0/24'), stdout=sub.PIPE)

def cleanString(x):
	for i in x:
		if i == "(":
			print i
	
ip    = getIP()
alive = scan()


print "[+] YOUR IP: %s " % (ip[0:12])
print("\n[+] DISPOSITIVOS CONECTADOS\n")
for row in alive.stdout:
    if ip in row.rstrip():
        print"[-] %s<== [YOU]"%str(row.rstrip()[20:])
        cont+=1
    elif "Nmap scan report for" in row.rstrip():
    	cleanString(str(row.rstrip()[21:]))
        print"[%i] %s"%(cont,str(row.rstrip()[21:]))
    	cont+=1

c = int(raw_input("Select one "))
print "Escaneando host %s"%dev_list[c]
