import sys


def main(argv):
    # argv[0] retorna o nome do arquivo (sum.py)
    num_1 = int(argv[1])
    num_2 = int(argv[2])
    sum_ = num_1 + num_2

    print("Soma de " + str(num_1) + " e " + str(num_2) + " = " + str(sum_))


if __name__ == '__main__':
    main(sys.argv)
