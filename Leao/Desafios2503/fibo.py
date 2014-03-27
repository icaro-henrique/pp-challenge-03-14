import sys


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

x = int(sys.argv[1])
print (fibonacci(x))
