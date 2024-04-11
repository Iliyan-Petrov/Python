import json

with open('Person.json', 'r') as json_file:
	json_object = json.load(json_file)

print(json_object)
