import sys
import os


def main():
    files = sys.argv[1:]
    for file_name in files:
        os.system("python3 cat.py %s" % file_name)

if __name__ == '__main__':
    main()
