#!/usr/bin/env python3

import random
import requests
import string
from base64 import b64decode
from urllib.parse import unquote


url = "http://10.10.11.119/register.php"

prev = 0
print(f'Name len   base64 c len   raw c len')
for i in range(1, 50):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(i))
    resp = requests.post(url, data={"username": name, "password": "aaaaa", "password2": "aaaaa"}, allow_redirects=False)
    b64_cookie = unquote(resp.cookies["auth"])
    raw_cookie = b64decode(b64_cookie)
    if len(b64_cookie) != prev:
        print(f'{len(name):^8}   {len(b64_cookie):^12}   {len(raw_cookie):^9}')
        prev = len(b64_cookie)
