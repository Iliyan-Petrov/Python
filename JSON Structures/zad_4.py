import json

data = {
  "name": "John",
  "age": 12,
  "children": None
}
JSONString = json.dumps(data)
print(JSONString)
