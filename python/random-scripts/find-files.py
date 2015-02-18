import os

for base, dirs, files in os.walk('/home/'):
	if "Challenges" in base:
		print base