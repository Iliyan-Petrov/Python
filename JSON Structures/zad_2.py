import json

jsonString = '{ "name": "Bob", "languages": ["English", "Fench"]}'
pDict = json.loads(jsonString)
print(pDict)
print(pDict['name'])
print(pDict['languages'])
