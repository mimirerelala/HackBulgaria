import sys

def main():
	res = 0
	filename = sys.argv[1]
	with open(filename, 'r') as data:
		numbers = data.read().split(' ')
		for num in numbers:
			res += int(num)
	print(res)
	return res


if __name__ == '__main__':
	main()


#Zapazvae na danni v filove
#open(filename, mode)
#			modes - r, w, a, r+
#
#
#
#close