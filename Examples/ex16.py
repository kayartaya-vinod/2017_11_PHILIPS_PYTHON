# multiple inheritance example


def main():
	h1 = Helicopter()
	h1.info()
# base/super classes

class Vehicle(object):
	def __init__(self, **kwargs):
		print("from inside of Vehicle.__init__()")
	def info(self):
		print("No information about Vehicle available")

class Flyable(object):
	def __init__(self, **kwargs):
		print("from inside of Flyable.__init__()")
	def info(self):
		print("No information about Flyable available")

class Helicopter(Vehicle, Flyable):
	def __init__(self, **kwargs):
		# super().__init__(**kwargs)
		Vehicle.__init__(self, **kwargs)
		Flyable.__init__(self, **kwargs)
		print("from inside of Helicopter.__init__()")

	def info(self):
		Vehicle.info(self)
		Flyable.info(self)

if __name__ == '__main__':
	main()


