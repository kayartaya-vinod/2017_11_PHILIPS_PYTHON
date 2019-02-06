# using if-else constructs
"In this module, we are testing the usage of if-else constructs."


# import ex03
# dir(ex03)
# help(ex03)
# help(ex03.main)

def main():
	
	'''This is the main function of the module.
	This accepts two numbers and tests which number is bigger than the other.
	'''

	n1 = int(input("Enter a number: "))
	n2 = int(input("Enter a number: "))


	if n1>n2: big = n1 
	else: big = n2

	print("Biggest of {} and {} is {}".format(n1, n2, big))


if __name__ == '__main__':
	main()




