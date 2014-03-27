import sys

def fib(valor): 
    a, b = 0, 1
    i = 0
    while i < valor:
        print(b)
        a, b = b, a+b
        i = i + 1
fib(int(sys.argv[1]))
