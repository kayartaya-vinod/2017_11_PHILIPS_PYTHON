def fibo(index=1): 
	a = -1
	b = 1
	for i in range(index):
		c = a+b
		a = b
		b = c
	return c

def fibo_between_indexes(start=1, stop=10):
	for i in range(start, stop+1):
		f = fibo(i)
		print("fibonacci value at index {} is {}".format(i, f))

def main():
	try: 
		first_index = int(input("Enter starting index: "))
		last_index = int(input("Enter ending index: "))
		fibo_between_indexes(first_index, last_index)
	except ArithmeticError as ex:
		print("There was an arithmetic error!", ex)
	except ValueError as ex:
		print("The input was of an incompatible type", ex)
	except BaseException as ex:
		print("There was an error!", ex)

	

if __name__ == '__main__':
	main()