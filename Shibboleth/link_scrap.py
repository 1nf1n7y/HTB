from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin

URL = sys.argv[1]
page = requests.get(URL,verify=False)

soup = BeautifulSoup(page.content, "html.parser")

links = [URL + a['href'] for a in soup.find_all("a", href=True)]
for link in (set(links)):
	print(link)
