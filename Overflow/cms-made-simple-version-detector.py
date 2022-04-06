import requests
import sys

URL = sys.argv[1]
req = requests.get(URL + "/doc/CHANGELOG.txt")
page = req.text
print(page.partition('\n')[0])
