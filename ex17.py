import requests

p1 = dict(first_name = "Pranav",
	last_name = "Kumar",
	dob = "1992-08-02",
	city = "Vasco",
	email = "pranavkumar@vinod.co",
	phone = "0982726262")

d1 = {"Content-Type" : "application/json", 
	"Accept" : "application/json"}

d2 = {"http" : "http://165.225.96.34:9480"}

url = "http://kelutral.com/rest/contacts.php"

resp = requests.post(url, json=p1, headers = d1) #, proxies = d2)

print(resp.json())