from bs4 import BeautifulSoup
from pathlib import Path

with open('date.txt', 'r') as f:
	date = f.read().strip()

path = Path('public/')
html_files = list(path.rglob('*.html'))

for file in html_files:
	with open(file, 'r') as f:
		data = f.read()

	page = BeautifulSoup(data, 'html.parser')

	links = page.find_all('a')
	for link in links:
		if "OFFLINE_DOWNLOAD" in link['href']:
			link['href'] = f"/static/bible-{date}.zip"

	with open(str(file), 'w') as f:
		f.write(str(page))

	print(f"Processed page: {str(file)}")

print(f"Total pages processed: {len(html_files)}")
