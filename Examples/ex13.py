class Person:
	# constructor for a class, automaticall executed for
	# every object creation
	def __init__(self, name=None, email=None):
		# a dunder member is considered to be a private member
		self.__name = name
		self.__email = email

	def info(self):
		print("Name =", self.__name)
		print("Email=", self.__email)

def main():
	p1 = Person("Vinod", "vinod@vinod.co") # p1 = new Person() in Java/C++/C#
	p2 = Person("John Doe", "johndoe@mail.com")
	p3 = Person("Jane Doe")
	p4 = Person()

	# the invoking object (p1 here) will be passed
	# as the very first argument, implicitly
	# does not affect the actual __name of p1
	p1.__name = "xyz" # creates a new member called __name
	print("inside main(), p1.__name is ", p1.__name)
	p1.info()
	p2.info()
	p3.info()
	p4.info()

if __name__ == '__main__':
	main()




