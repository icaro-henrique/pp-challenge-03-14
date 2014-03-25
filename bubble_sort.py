import sys


def main(args):
    unsorted = []
    for num in args[1:]:
        unsorted.append(int(num))

    print("Unsorted list: " + str(unsorted))

    for pos_x in range(len(unsorted)):
        for pos_y in range(len(unsorted)):
            if unsorted[pos_x] < unsorted[pos_y]:
                aux = unsorted[pos_x]
                unsorted[pos_x] = unsorted[pos_y]
                unsorted[pos_y] = aux

    sorted_ = unsorted
    print("Sorted list: " + str(sorted_))


if __name__ == '__main__':
    main(sys.argv)
