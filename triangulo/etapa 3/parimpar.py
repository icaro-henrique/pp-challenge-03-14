import sys
import random

random.seed()
input1 = int(sys.argv[1])
escolhacpu = random.randint(1, 2)
input2 = sys.argv[2]
resultado = (input1 + escolhacpu) % 2
if resultado == 0 and input2 == "par":
    print("Voce ganhou")
elif resultado == 0 and input2 == "impar":
    print("cpu ganhou")
elif resultado != 0 and input2 == "par":
    print("cpu ganhou")
else:
    print("Voce ganhou")
