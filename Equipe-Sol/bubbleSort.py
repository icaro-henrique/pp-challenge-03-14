import sys

def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[ j ] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
list = []
for i in range(1,len(sys.argv)):
	list.append(int(sys.argv[i]))

lista = bubble_sort(list)

print(lista)

