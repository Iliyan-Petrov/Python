import socket
import re

url = input("Please enter URL: ")
hostname = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
if len(hostname) == 0:
	print("Invalid URL entered")
	exit()

hostname = hostname[0][7:]
port = 80

try:
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((hostname, port))
	client_socket.sendall(f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n".encode())

	received_data = b''
	while True:
    	data = client_socket.recv(1024)
    	if not data:
        	break
    	received_data += data
    	if len(received_data) > 300:
        	break

	received_data = received_data.decode()
	total_chars = len(received_data)
	received_data = received_data[:300]

	print(received_data)
	print(f"\n\nTotal number of characters: {total_chars}")

except Exception as e:
	print(f"Error connecting to server: {e}")
finally:
	client_socket.close()
