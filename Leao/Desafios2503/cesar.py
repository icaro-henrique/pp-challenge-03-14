import sys


x = sys.argv[1]
n = int(sys.argv[2])
cesar = []
i = 0
aux = ""
list
for i in range(0, len(sys.argv[1])):
    if (ord(x[i]) > 122) or (ord(x[i]) < 97):
        print ("Letra(s) invalida(s)")
        sys.exit()
    elif (ord(x[i]) + n > 122):
        aux = chr(ord(x[i])+n-26)
        cesar.append(aux)
    else:
        cesar.append(chr(ord(x[i]) + n))
cesar = ''.join(cesar)
print(cesar)
