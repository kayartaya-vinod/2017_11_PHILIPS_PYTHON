class Employee(object):
	def __init__(self, **kwargs):
		self.__id = kwargs["id"] if "id" in kwargs else None
		self.__name = kwargs["name"] if "name" in kwargs else None
		self.__salary = kwargs["salary"] if "salary" in kwargs else 15000

	# getter (readable) property
	@property
	def salary(self):
		return self.__salary

	# setter exists only for getter properties
	# setter (writable) property
	@salary.setter
	def salary(self, new_salary):
		if new_salary < self.__salary:
			raise ValueError("New salary must be >= Rs.{}".format(self.__salary))
		self.__salary = new_salary

	def info(self):
		print("Id =", self.__id)
		print("Name =", self.__name)
		print("Salary = Rs.", self.__salary)
		print("."*40)

	def __mul__(self, num):
		return self.__salary * num

	def __iadd__(self, value):
		if type(value) == str:
			self.__name += value
		elif type(value) in [int, float]:
			self.__salary += value
		return self

	def __lt__(self, value):
		if type(value)==str:
			return self.__name < value
		elif type(value) in [int, float]:
			return self.__salary < value
		# elif  type(value) == type(self):
		elif  type(value) == Employee:
			return self.__salary < value.__salary
		else:
			raise TypeError(
				"Type '{}' is not supported for this operation!".format(
					type(value)))

	def author_info():
		print("Name: Vinod Kumar")
		print("Email: vinod@vinod.co")

def main():
	e1 = Employee(id=7788, name="John", salary = 25000)
	e2 = Employee(id=7123, name="Jane Doe", salary = 34000)

	e1.info()

	print("Yearly salar of e1 is Rs.", e1*12) # expecting e1.salary multiplied by 12 without mutating
	print("e1 < e2 is", e1<e2) # expecting salaries of e1 and e2 being compared
	print("e1 < 'Jane' is", e1<'Jane') # expecting salaries of e1 and e2 being compared
	print("e1 < 45000 is", e1<15000) # expecting salaries of e1 and e2 being compared
	e1 += " Doe" # expecting " Doe" to be appended to e1.name
	e1 += 5000 # expecting 5000 to be added to e1.salary

	e1.info()

def main1():
	e1 = Employee(id=7788, name="John Doe", salary = 20000)
	e2 = Employee(id=7123, name="Jane Doe", salary = 34000, dept="ADMIN")

	e1.info() # python invokes info() by supplying "e1" as first arg
	# e2.info()
	Employee.info(e2) # we invoke info() by supplying "e2" as first arg

	# salary although is a function, treated as a variable
	print("salary of e2 is ", e2.salary) # e2.salary --> readable property
	e2.salary = 55000 # e2.salary --> writable property

	e2.info()


if __name__ == '__main__':
	main()

