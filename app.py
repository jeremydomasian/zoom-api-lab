#!/usr/bin/env python3

from flask import Flask, request, redirect
import requests
import os
import base64

client_id = os.environ.get('ZOOM_CLIENT_ID')
client_secret = os.environ.get('ZOOM_CLIENT_SECRET')
redirect_uri = 'http://localhost:8080/oauth/redirect' 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Zoom OAuth Test'

@app.route('/oauth/redirect')
def oauth_redirect():
    code = request.args.get('code')
    if code:
        token_url = 'https://zoom.us/oauth/token'
        auth_header = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
        headers = {
             'Authorization': f'Basic {auth_header}'
        }
        params = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
          }
        response = requests.post(token_url, headers=headers, params=params)

        if response.status_code == 200:
            access_token = response.json().get('access_token')
            refresh_token = response.json().get('refresh_token')
            # You can use access_token to make authenticated requests
            # And save refresh_token securely for later use
            return f'Access Token: {access_token}'
            # return f'Access Token: {access_token}\nRefresh Token: {refresh_token}'
        else:
            return f'Error fetching access token: {response.text}', response.status_code
    else:
        return 'No code provided', 400

if __name__ == '__main__':
    app.run(port=8080)
