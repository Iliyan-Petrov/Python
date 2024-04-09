#v.1

import urllib.parse
import urllib.request

url = input("Enter URL: ")
try:
	parts = urllib.parse.urlsplit(url)
	if not all([parts.scheme, parts.netloc]):
    	raise ValueError("Malformed URL")
except ValueError as e:
	print("Error:", e)
else:
	try:
    	with urllib.request.urlopen(url) as response:
        	page = response.read().decode()
    	print(page)
	except urllib.error.URLError as e:
    	print("Error:", e)


#v.2
import urllib.parse
import urllib.request


def retrieve_webpage(url):
	try:
    	parsed_url = urllib.parse.urlparse(url)
    	hostname = parsed_url.hostname
    	path = parsed_url.path

    	if not hostname:
        	print("Error: Malformed URL. Please enter a valid URL with a hostname.")
        	return
    	conn = urllib.request.urlopen(url)
    	page_data = conn.read()

    	print("First 300 characters:")
    	print(page_data[:300])
    	print()

    	num_chars = len(page_data)
    	print("Number of characters:", num_chars)

	except urllib.error.HTTPError as e:
    	print("Error: Failed to retrieve web page.")
    	print(e)


url = input("Enter a URL to retrieve: ")
retrieve_webpage(url)
