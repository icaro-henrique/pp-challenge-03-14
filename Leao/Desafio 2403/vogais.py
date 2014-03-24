import sys

f = open('nome.txt', 'r')
ler = f.read()
f.close()
contador = 0
i = 0

print(ler)
for caracter in ler:
    if caracter in 'aeiou':
        contador = contador + 1

print (contador)
