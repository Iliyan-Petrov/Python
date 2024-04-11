import json

json_data = '''
{
	"name": "John Doe",
	"age": 30,
	"email": "johndoe@example.com",
	"hobbies": ["reading", "traveling", "hiking"]
}
'''

try:
    parsed_data = json.loads(json_data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON data: {e}")
else:

    print("Parsed JSON data:")
    print(f"Name: {parsed_data['name']}")
    print(f"Age: {parsed_data['age']}")
    print(f"Email: {parsed_data['email']}")
    print(f"Hobbies: {', '.join(parsed_data['hobbies'])}")
