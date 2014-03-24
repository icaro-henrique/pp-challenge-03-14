p = input('Digite a palavra: ')
a = 0
e = 0
i = 0
o = 0
u = 0
p = p.lower()
for l in p:
    if l == 'a':
        a += 1
    if l == 'e':
        e += 1
    if l == 'i':
        i += 1
    if l == 'o':
        o += 1
    if l == 'u':
        u += 1
print ('Número de vogais a: %s' % a)
print ('Número de vogais e: %s' % e)
print ('Número de vogais i: %s' % i)
print ('Número de vogais o: %s' % o)
print ('Número de vogais u: %s' % u)
