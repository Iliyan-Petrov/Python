def get_users():
    users = [
   	 {'id': 1, 'name': 'John Doe', 'email': 'johndoe@gmail.com'},
   	 {'id': 2, 'name': 'Jane Doe ', 'email': 'janedoe@gmail.com'},
   	 {'id': 3, 'name': 'Bob Smith', 'email': 'bobsmith@gmail.com'},
    ]
    return users

users_list = get_users()
for users in users_list:
    for key, value in users.items():
        print(f"{key}: {value} \n")