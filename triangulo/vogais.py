import sys

vowels = "aeiou"
for v in vowels:
    print(v, sys.argv[1].lower().count(v))
