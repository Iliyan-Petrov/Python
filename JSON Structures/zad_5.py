import json

data = \
 {
"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

JSONString = json.dumps(data)

with open('json_data.json', 'w') as outfile:
 outfile.write(JSONString)
