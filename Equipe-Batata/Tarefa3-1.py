def fib(n):
	if n < 2:
		return n
	else:
		return (fib(n - 1) + fib(n - 2))

numero = int(input("Informe o numero: "))
print("n-esimo numero de Fibonacci: %s" % fib(numero))