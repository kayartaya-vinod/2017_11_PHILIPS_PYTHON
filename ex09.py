import json

def json_to_csv(json_filename):
	with open(json_filename) as jfile:
		people = json.load(jfile)

		s = "\n".join(['"{name}","{city}"'.format(**p) for p in people])
		with open("out.csv", "w") as f:
			f.write(s)

		print("CSV file saved!")



def csv_to_json(csv_filename, json_filename, indt=None):
	with open(csv_filename, encoding="UTF-8") as csv:
		filednames = csv.readline().rstrip().split(",")
		d=[dict(zip(filednames, line.rstrip().split(","))) for line in csv]
		with open(json_filename, "w") as jfile:
			# jfile.write(json.dumps(d, indent=indt))
			json.dump(d, jfile)

def main1():
	csv_filename = input("Enter CSV filename: ")
	json_filename = input("Enter JSON filename: ")
	csv_to_json(csv_filename, json_filename, 4)
	print("File saved successfully!")

def main():
	json_filename = input("Enter JSON filename: ")
	json_to_csv(json_filename)

if __name__ == '__main__':
	main()
