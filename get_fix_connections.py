import requests

from auth import get_token  # see auth.py for more details

FIX_CONNECTIONS_URL = 'https://api.factioninc.com/v2/fix/connections'
ORGANIZATION_ID = 'b356915e-8083-4ca3-8853-9b2bdadecef9'

token = get_token()


def get_fix_connections():
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Organization-Id': ORGANIZATION_ID,
    }
    fix_connections_response = requests.get(url=FIX_CONNECTIONS_URL, headers=headers)
    fix_connections = fix_connections_response.json()
    return fix_connections


if __name__ == '__main__':
    fix_connections = get_fix_connections()
    print('FIX Connections:')
    print(fix_connections)
