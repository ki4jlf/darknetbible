from bs4 import BeautifulSoup
from pathlib import Path

# Create an offline readable version of the bible in offline/

# This script depends on beautifulsoup4:
# ~ apt install python3-pip
# ~ pip3 install beautifulsoup4


path = Path('offline/')
html_files = list(path.rglob('*.html'))

URL = "http://biblemeowimkh3utujmhm6oh2oeb3ubjw2lpgeq3lahrfr2l6ev6zgyd.onion"


def fix_link(link):
	return link.replace(URL, "")[1:] + "index.html"


def traversal(number):
	return "../" * number + "content/"


for file in html_files:
	with open(file, 'r') as f:
		data = f.read()

	page = BeautifulSoup(data, 'html.parser')

	path_depth = max(0, len(str(file).split('/')) - 2)

	links = page.find_all('a')
	for link in links:
		if URL in link['href'] or link['href'][0] == "/":
			link['href'] = traversal(path_depth) + fix_link(link['href'])

	imgs = page.find_all('img')
	for img in imgs:
		img['src'] = traversal(path_depth) + img['src'].strip('/')

	css = page.find('link', attrs={'rel': 'stylesheet'})
	if css:
		css['href'] = traversal(path_depth) + css['href'].strip('/')
		del css['integrity']

	with open(str(file), 'w') as f:
		f.write(str(page))

	print(f"Processed page: {str(file)}")

print(f"Total pages processed: {len(html_files)}")
