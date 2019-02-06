"""
Accept a month and year, and print the number of days in it
"""

def max_days(month=1, year=2017):
	"""
	This function can be called in the following ways:
	1. d = max_days(2, 2018)
	2. d = max_days(2)
	3. d = max_days(year=2018)
	4. d = max_days(year=2018, month=3)
	5. d = max_days(month=2)
	6. d = max_days()
	"""

	if(type(month) is not int):
		raise TypeError("Invalid datatype for 'month'")
		
	if(type(year) is not int):
		raise TypeError("Invalid datatype for 'year'")

	if month in {4, 6, 9, 11}:
		days = 30
	elif month in [1, 3, 5, 7, 8, 10, 12]:
		days = 31
	elif month == 2:
		condition = year%400==0 or (year%4==0 and year%100!=0)
		days = 29 if condition else 28
	else:
		raise ValueError("Invalid value for 'month'")

	return days

def main():
	d = max_days(2, 2020)
	print("max days = {}\n".format(d))
	
	d = max_days(2)
	print("max days = {}\n".format(d))
	
	d = max_days(year=2018)
	print("max days = {}\n".format(d))
	
	d = max_days(year=2018, month=3)
	print("max days = {}\n".format(d))
	
	d = max_days(month=2)
	print("max days = {}\n".format(d))
	
	d = max_days()
	print("max days = {}\n".format(d))




if __name__ == '__main__':
	main()