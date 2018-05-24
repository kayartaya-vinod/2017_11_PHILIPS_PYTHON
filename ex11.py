def add_name(name, names = []):
	names.append(name)
	return names

if __name__ == '__main__':
	add_name("Vinod")
	add_name("Shyam")
	add_name("Satya")
	lst = add_name("Uday")

	print("lst contains", lst)