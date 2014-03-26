import sys
from random import randint

i = randint(1,2)
if((int(sys.argv[1])!= 1) and (int(sys.argv[1])!= 2) ):
	print("\nDados de entrada incorretos")
if(sys.argv[2].lower()=="par"):
	if((int(sys.argv[1]) + i) % 2 == 0):
		print("\nVitoria: voce jogou par e %s contra impar e %i" % (sys.argv[1], i))
	else:
		print("\nDerrota: voce jogou par e %s contra impar e %i" % (sys.argv[1], i))
elif(sys.argv[2].lower()=="impar"):
	if((int(sys.argv[1]) + i) % 2 == 1):
		print("\nVitoria: voce jogou impar e %s contra par e %i" % (sys.argv[1], i))
	else:
		print("\nDerrota: voce jogou impar e %s contra par e %i" % (sys.argv[1], i))
else:
	print("\nDados de entrada incorretos") 