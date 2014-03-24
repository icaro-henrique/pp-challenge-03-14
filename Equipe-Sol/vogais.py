import sys

counta = 0
counte = 0
counti = 0
counto = 0
countu = 0

vowels = "aeiuo"
for letter in sys.argv[1].lower():
    if letter in vowels:
        if letter == "a":
            counta += 1
        if letter == "e":
            counte += 1
        if letter == "i":
            counti += 1
        if letter == "o":
            counto += 1
        if letter == "u":
            countu += 1

print("A:", counta)
print("E:", counte)
print("I:", counti)
print("O:", counto)
print("U:", countu)
