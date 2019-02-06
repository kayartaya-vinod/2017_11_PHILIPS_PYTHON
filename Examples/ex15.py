from ex13 import Person

class Customer(Person):

	def __init__(self, **kwargs):
		name = kwargs["name"] if "name" in kwargs else None
		email = kwargs["email"] if "email" in kwargs else None
		# Person.__init__(self, name, email)
		super().__init__(name, email)

		self.__id = kwargs["id"] if "id" in kwargs else None
		self.__phone = kwargs["phone"] if "phone" in kwargs else None

	# method overriding is allowed
	def info(self):
		print("Id = ", self.__id)
		super().info() # same as Person.info(self)
		# Person.info(self)
		print("Phone = ", self.__phone)
		print("-"*20)

def main():
	c1 = Customer(name="vinod", email="viond@vinod.co", id=123, phone="9731424784")
	c1.info()

if __name__ == '__main__':
	main()