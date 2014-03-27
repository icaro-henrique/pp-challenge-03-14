from random import randint
import sys

def parImpar(word, number):
    n = int(number)
    word.lower()
    nRand = randint(1,2)
    if word == 'par':
        if (n+nRand) % 2 == 0 :
            return('PC Jogou: %i Você jogou: %i VOCE VENCEU ' % (nRand,n))
        else:
            return('PC Jogou: %i Você jogou: %i VOCE PERDEU ' % (nRand,n))
    if word == 'impar':
        if (n+nRand) % 2 == 1 :
            return('PC Jogou: %i Você jogou: %i VOCE VENCEU ' % (nRand,n))
        else:
            return('PC Jogou: %i Você jogou: %i VOCE PERDEU ' % (nRand,n))

print(parImpar(sys.argv[1], sys.argv[2]))
