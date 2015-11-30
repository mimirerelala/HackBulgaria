import sys

def main():

	filename = sys.argv[1]
	data = open(filename, 'r')
	print(data.read())


if __name__ == '__main__':
	print(main())


#Zapazvae na danni v filove
#open(filename, mode)
#			modes - r, w, a, r+
#
#
#
#close