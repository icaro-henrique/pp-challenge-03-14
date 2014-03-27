import sys


def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

countElements = len(sys.argv)
myArray = []
for x in range(1, countElements):
    myArray.append(int(sys.argv[x][:]))
bubble(myArray)
print(str(myArray))
