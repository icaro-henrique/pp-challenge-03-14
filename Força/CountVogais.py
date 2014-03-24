a = open("nome.txt")

texto = a.read()

a = 0
e = 0
o = 0
i = 0
u = 0

for caracter in texto:
    if caracter in 'aA':
        a = a + 1
    if caracter in 'eE':
        e = e + 1
    if caracter in 'iI':
        i = i + 1
    if caracter in 'oO':
        o = o + 1
    if caracter in 'uU':
        u = u + 1

print ("A: ", a)
print ("E: ", e)
print ("I: ", i)
print ("O: ", o)
print ("U: ", u)
