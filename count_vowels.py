from collections import defaultdict


def main():
    string = raw_input('Digite o texto: ').lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = defaultdict(int)

    for char in string:
        if char in vowels:
            counts[char] += 1

    print counts.items()


if __name__ == '__main__':
    main()
