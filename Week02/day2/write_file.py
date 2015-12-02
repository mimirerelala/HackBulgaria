import sys

def main():

	filename = sys.argv[1]

	data = open(filename, 'w')
	#with open(filenmae, "w") as data:   alternaritvely, no close statement ../
	data.write("I am a panda :) \n")
	data.close()


if __name__ == '__main__':
	main()


#Zapazvae na danni v filove
#open(filename, mode)
#			modes - r, w, a, r+
#
#
#
#close