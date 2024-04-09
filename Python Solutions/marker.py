import requests

url = input()
start_byte = 1
end_byte = 100

headers = {'Range': f'bytes={start_byte}-{end_byte}'}
response = requests.get(url, headers=headers)

with open('first_100_bytes.txt', 'wb') as f:
	f.write(response.content)

file_size = int(response.headers.get('content-length'))
start_byte = file_size - 100
end_byte = file_size - 1

headers = {'Range': f'bytes={start_byte}-{end_byte}'}
response = requests.get(url, headers=headers)

with open('last_100_bytes.txt', 'wb') as f:
	f.write(response.content)
