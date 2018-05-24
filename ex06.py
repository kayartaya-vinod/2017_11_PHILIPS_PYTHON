# program to test the while loops

def main():
	n = int(input("Enter a number: "))
	m = n
	f = 1

	while n>0:
		f *= n # f = f * n
		n -= 1 # n = n - 1

	print("Factorial of {} is {}\n".format(m, f))

if __name__ == '__main__':
	main()