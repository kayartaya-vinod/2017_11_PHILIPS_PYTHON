# using if-else constructs
"In this module, we are testing the usage of if-else constructs."


def main():

	'''This is the main function of the module.
	This accepts three numbers and tests which number is bigger than the other two.
	'''

	n1 = int(input("Enter a number: "))
	n2 = int(input("Enter a number: "))
	n3 = int(input("Enter a number: "))


	if n1>n2 and n1>n3:
		big = n1
	elif n2>n3:
		big = n2
	else:
		big = n3

	print("Biggest of {}, {} and {} is {}".format(n1, n2, n3, big))


if __name__ == '__main__':
	main()




