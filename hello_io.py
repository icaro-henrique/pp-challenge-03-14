def main():
    file_with_name = open("name.txt", 'r')

    print "Hello, " + file_with_name.readline()

    file_with_name.close()


def main_alt():
    """
    Palavra "with" controla o contexto do arquivo aberto,
    ele eh fechado em caso de erro e no fim do bloco.
    Preferivel fazer leitura de arquivos desta maneira
    """
    with open("name.txt", 'r') as file_with_name:
        print "Hello, " + file_with_name.readline()


if __name__ == '__main__':
    main()
