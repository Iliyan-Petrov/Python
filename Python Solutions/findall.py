import re
string = input()
addresses = re.findall(r'(https?://[^\s]+)', string)
print(addresses)
