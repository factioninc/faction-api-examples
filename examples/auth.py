import requests

TOKEN_URL = 'https://auth.factioninc.com/as/token'
CLIENT_ID = '<Your Client ID>'
CLIENT_SECRET = '<Your Client Secret>'


def get_token():
    request_body = {'grant_type': 'client_credentials'}
    auth = (CLIENT_ID, CLIENT_SECRET)
    response = requests.post(url=TOKEN_URL, auth=auth, data=request_body)
    response_body = response.json()
    token = response_body['access_token']
    return token
