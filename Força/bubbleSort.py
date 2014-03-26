import sys

def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[ j ] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = []
k = 1
while k < len(sys.argv):
    lista.append(int(sys.argv[k]))
    k = k + 1
    
print (bubble_sort(lista))
    
