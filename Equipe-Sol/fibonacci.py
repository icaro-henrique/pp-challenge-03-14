import sys

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for x in range(int(sys.argv[1])):
    print(fibonacci(x))