#!/usr/bin/env python3

import requests

for api_key in range(1, 100, 2):
    print(f"api_key {api_key}")
    # You should add a colon after the for loop line, and use 'http://' instead of 'http//'
    html = requests.get(f'http://machine_ip/api/{api_key}')
    print(html.text)
