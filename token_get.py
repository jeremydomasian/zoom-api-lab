#!/usr/bin/env python3

import os
import webbrowser

client_id = os.environ.get('ZOOM_CLIENT_ID')
redirect_uri = os.environ.get('ZOOM_REDIRECT_URI')

auth_url = f'https://zoom.us/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'

webbrowser.open(auth_url)