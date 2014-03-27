import sys
from random import randint

parImpar = int(sys.argv[2])
parImparRandom = randint(1,2)
somaparImpar = (parImpar + parImparRandom)

if(sys.argv[1] == "par" and somaparImpar % 2==0 or sys.argv[1] == "impar" and somaparImpar % 2==1):
	print("Venceu!\n Adversário: ", parImparRandom)
else:
	print("Loserrrrr :p\nAdversário: ", parImparRandom)