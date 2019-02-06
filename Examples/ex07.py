# Pyramid of stars

num = int(input("Enter a number: "))

for i in range(num):
	for j in range(i+1):
		print("* ", end="")
		# print "* " ,  #<---- for python 2.7 (end with a comma)

	print() # <----- for printing a new line