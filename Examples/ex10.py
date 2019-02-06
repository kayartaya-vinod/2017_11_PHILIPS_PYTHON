# function arguments (formal/actual)

def test_args(name, city="Bangalore", *args, **kwargs):
	print("name=",name)
	print("args=",args)
	print("kwargs=",kwargs)
	print("city=",city)
	print("-"*50)	

def main():
	test_args("Vinod")
	test_args("Vinod", city="Shimoga")
	test_args("Vinod", "Vinu", "VK", city="Shivamogga")
	test_args("Vinod", "Vinu")
	test_args("Vinod", city="Bengaluru", age=44)

def test_args_3(**kwargs):
	print("typeof kwargs is", type(kwargs))
	print("kwargs contain:", kwargs)
	print("-"*50)	

def main_3():
	test_args_3(name="Vinod", email="vinod@vinod.co")
	test_args_3(subject="maths", max_marks=100, marks= 67)
	test_args_3()

	d = dict(x=100, y=200, z=400)
	test_args_3(**d)

def test_args_2(*args):
	print("typeof args is", type(args))
	print("args contain:", args)
	print("-"*50)

def main_2():
	test_args_2("Vinod", "Bangalore")
	test_args_2(100, 200, 300, 400)


def test_args_1(name, city="Bangalore", state="Karnataka", country="India"):
	print("typeof name is ", type(name))
	print("name = ", name)
	print("city = ", city)
	print("state = ", state)
	print("country = ", country)
	print("-"*50)



def main_1():
	test_args_1("Vinod")
	test_args_1("Pranav", state="Goa", city="Vasco")

	# len of t1 must be >= non-default params and <= all params
	t1 = ("Smith", "Dallas")
	test_args_1(*t1)

	# len of t1 must be >= non-default params and <= all params
	t1 = ("John", "Dallas", "Texas", "USA")
	test_args_1(*t1)

	# len of l1 must be >= non-default params and <= all params
	l1 = ["Jane", "Dallas", "Texas", "USA"]
	test_args_1(*l1)

	# dict keys must match the argument names
	p1 = dict(name="Ashish", country="Bhrarath")
	test_args_1(**p1)


if __name__ == '__main__':
	main()