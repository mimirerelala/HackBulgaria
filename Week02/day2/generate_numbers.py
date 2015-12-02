# generate_numbers.py
import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    string_to_append = ""
    if n > 0:
        string_to_append += str(randint(1, 1000))
    for i in range(1, n):
        string_to_append += " "
        string_to_append += str(randint(1, 1000))

    with open(filename, 'w') as to_write:
        to_write.write(string_to_append)
    return

if __name__ == '__main__':
    main()
