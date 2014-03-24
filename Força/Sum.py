import sys


def printinfo(X, Y):
    print ("X = ", X)
    print ("Y = ", Y)
    print (int(X)+int(Y))
    return

printinfo(sys.argv[1], sys.argv[2])
