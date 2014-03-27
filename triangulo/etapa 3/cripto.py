import sys

chave = int(sys.argv[2])

original = sys.argv[1]
original = original.lower()
cripto = []
for character in original:
    number = ord(character)
    number = number + chave
    cripto.append(number)
print(''.join(chr(i) for i in cripto))
