import sys
import random

num = int(sys.argv[1])
pi = sys.argv[2]
resultPi = ""
rand = random.randint(0, 2)

resultNu = (num + rand) % 2

if resultNu == 0:
    resultPi = "Par"
else:
    resultPi = "Impar"

print (rand, "\n")
print ("total:", num + rand, "\n")

if resultPi == pi:
    print (resultPi, "Voce ganhou!")
else:
    print (resultPi, "Voce Perdeu")
