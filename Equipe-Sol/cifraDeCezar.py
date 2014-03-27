import string
import sys

alfabeto = "abcdefghijklmnopqrstuvwxyz"
chave =int(sys.argv[2])
palavraFinal = ""
palavra = sys.argv[1].lower()
tamAlfabeto = len(alfabeto)

for i in range(0,len(palavra)):
	pos = alfabeto.index(palavra[i]) + chave
	while(len(alfabeto) < pos):
		
		if(pos > tamAlfabeto):
			pos = pos % tamAlfabeto
		else:
			break

	if(len(alfabeto) > pos):
		palavraFinal += alfabeto[pos]
	else:
		palavraFinal += palavra[i]
print(palavraFinal)
