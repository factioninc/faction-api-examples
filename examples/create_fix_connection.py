import requests

from auth import get_token  # see auth.py for more details

FIX_CONNECTIONS_URL = 'https://api.factioninc.com/v2/fix/connections'
ORGANIZATION_ID = '<Your Organization ID>'

token = get_token()


def create_fix_connection():
    fix_connection_data = {
        'connectionType': 'cloud',
        'connectionData': {
            'accountId': 'example-inc',
            'bandwidth': 10,
            'connectionSubType': 'aws_direct_connect',
            'crossCloudEnabled': False,
            'factionLocations': ['SV4'],
            'providerRegion': 'us-east-2',
        }
    }

    headers = {
        'Authorization': f'Bearer {token}',
        'X-Organization-Id': ORGANIZATION_ID,
    }
    fix_connections_response = requests.post(url=FIX_CONNECTIONS_URL, headers=headers, json=fix_connection_data)
    created_fix_connection = fix_connections_response.json()
    return created_fix_connection


if __name__ == '__main__':
    created_fix_connection = create_fix_connection()
    print('Created FIX Connection:')
    print(created_fix_connection)