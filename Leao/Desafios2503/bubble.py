import sys


def bubbleSort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                sorted = False
                t = a[i-1]
                a[i-1] = a[i]
                a[i] = t

x = 1
list = []
for x in range(1, len(sys.argv)):
    list.append(int(sys.argv[x]))
bubbleSort(list)

print(list)
