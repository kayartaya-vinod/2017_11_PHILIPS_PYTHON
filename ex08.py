# php like function
def file_get_content(filename):
	with open(filename) as file:
		return "".join(file)

def file_with_block():
	with open(fname, "rt") as file:
		for line in file:
			print(line, end="")

def display_file_content():
	file = open(fname, "rt")

	for line in file.readlines():
		# print(line, end="")
		print(line.rstrip())

	file.close()


if __name__ == '__main__':
	filename = input("Enter filename: ")
	content = file_get_content(filename)
	print(content)