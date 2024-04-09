import socket

def retrieve_webpage(url):
	try:
    	protocol, url = url.split('://')
    	host, path = url.split('/', 1)
    	path = '/' + path
	except ValueError:
    	print('Error: Invalid URL')
    	return

	try:
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	sock.connect((host, 80))
	except socket.error:
    	print('Error: Could not connect to server')
    	return

	request = f'GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n'
	sock.sendall(request.encode())

	response = b''
	while True:
    	data = sock.recv(1024)
    	if not data:
        	break
    	response += data

	sock.close()

	response = response.decode()
	headers, body = response.split('\r\n\r\n', 1)

	num_chars = 0
	for char in body:
    	if num_chars == 300:
        	print('... (more than 300 characters)')
        	break
    	print(char, end='')
    	num_chars += 1

	total_chars = len(response)
	print(f'\n\nTotal number of characters: {total_chars}')

url = input("Please enter URl: ")
retrieve_webpage(url)
