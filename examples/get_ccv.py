import requests
from auth import get_token  # see auth.py for more details

CCV_URL = 'https://api.factioninc.com/v1/ccv/volumes'
ORGANIZATION_ID = '<Your Organization ID>'

token = get_token()


def get_ccv():
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Organization-Id': ORGANIZATION_ID,
    }
    ccv_response = requests.get(url=CCV_URL, headers=headers)
    ccv_list = ccv_response.json()
    return ccv_list


if __name__ == '__main__':
    ccv_list = get_ccv()
    print('CCVs:')
    print(ccv_list)
