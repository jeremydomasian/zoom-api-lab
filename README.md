# zoom_api_lab
testing Zoom API calls

## What this currently does

Retrieves your own Zoom account information

## How to use this

0. Install dependencies: `flask`, `requests`
1. Create an OAuth app in Zoom App Marketplace with `user:read` scope
- Intend to publish: `No`
- User-managed app
- Scope: `user:read`
2. Add your app's Client ID (`ZOOM_CLIENT_ID`) and Client Secret (`ZOOM_CLIENT_SECRET`) to your environment variables
3. Run `app.py`
4. In another terminal session, run `token_get.py`
5. Log into Zoom in the new browser window
6. Copy the access token
7. Run `info_get.py`, paste the access token at the prompt, and hit Enter
