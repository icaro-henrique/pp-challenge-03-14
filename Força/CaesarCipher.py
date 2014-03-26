import sys

def caesar(word, number):
    n = int(number)
    lista = ('abcdefghijklmnopqrstuvwxyz')
    word.lower()
    newWord = ''
    for i in range (0, len(word)):
        for j in range(0, len(lista)):
            if word[i] == lista[j]:
                if (j+n) > len(lista)-1:
                    auxN = n - ((len(lista)-1)-j) - 1
                    newWord = newWord + lista[auxN]
                else:
                    newWord = newWord + lista[j+n]
    return newWord

print(caesar(sys.argv[1],sys.argv[2]))
                
