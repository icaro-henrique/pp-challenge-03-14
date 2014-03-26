import sys

lista = []
i = 1
flag = False
while(True):
	if flag == True:
		break
	try:
		lista.append(int(sys.argv[i]))
		i += 1
	except IndexError:
		flag = True
		i -= 1
aux = 0
for m in range(0,i):
	for j in range(0, i-1):
		if(lista[j]>lista[j+1]):
			aux = lista[j]
			lista[j] = lista[j+1]
			lista[j+1] = aux
for n in lista:
	print(n)

#print (sys.argv[1])
	