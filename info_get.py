#!/usr/bin/env python3

import requests

access_token = input("Enter your access token:")

user_id = 'me'  # 'me' refers to the current authenticated user
url = f'https://api.zoom.us/v2/users/me'

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    activities = response.json()
    print(activities)
else:
    print(f'Error: {response.status_code}')
    print(response.text)