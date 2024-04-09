import requests
from bs4 import BeautifulSoup


url = input("Please enter a URL:")
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
paragraphs = soup.find_all("p")
print(f"Total paragraphs found: {len(paragraphs)}")


for i, paragraph in enumerate(paragraphs):
	print(f"\nParagraph {i+1}:")
	print(paragraph.get_text())
