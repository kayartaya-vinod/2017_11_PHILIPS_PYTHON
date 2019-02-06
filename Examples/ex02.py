print("In ex02 value of __name__ is: {}".format(__name__))

# The name of the file is a.k.a the module name
# For example this file is a.k.a a modiule "ex02"

author_name = "Vinod Kumar"

# define a function
def say_hello(name):
 message = "Hello, "
 message += name
 message += "!!!"

 print(message)

def say_hi(name):
	message = "Hi, "
	message += name
	message += "!"

	print(message)

if __name__ == '__main__':
	# use a function (call)
	say_hello("Vinod")








