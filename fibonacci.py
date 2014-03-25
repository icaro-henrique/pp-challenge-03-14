import sys


def main(argv):
    quantity = int(argv[1])
    print("F" + str(quantity) + " = " + str(fib(quantity)))


def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)


if __name__ == '__main__':
    main(sys.argv)
