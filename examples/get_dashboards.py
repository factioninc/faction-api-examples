import requests
from auth import get_token  # see auth.py for more details

DASHBOARDS_URL = 'https://api.factioninc.com/v1/dashboards'
WIDGET_URL = 'https://api.factioninc.com/v1/dashboards/{dashboard_id}/widgets/{widget_id}'
ORGANIZATION_ID = '<Your Organization ID>'

token = get_token()


def get_dashboards():
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Organization-Id': ORGANIZATION_ID,
    }
    dashboards_response = requests.get(url=DASHBOARDS_URL, headers=headers)
    dashboards = dashboards_response.json()
    return dashboards


def get_dashboard_widget(dashboard_id, widget_id):
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Organization-Id': ORGANIZATION_ID,
    }
    widget_url = WIDGET_URL.format(dashboard_id=dashboard_id, widget_id=widget_id)
    widget_response = requests.get(url=widget_url, headers=headers)
    widget = widget_response.json()
    return widget


if __name__ == '__main__':
    dashboards = get_dashboards()
    print('Dashboards:')
    print(dashboards)

    dashboard = dashboards[0]
    dashboard_id = dashboard['identifier']
    dashboard_widgets = dashboard['widgetsConfig']
    widget_info = dashboard_widgets[0]
    widget_id = widget_info['identifier']

    widget = get_dashboard_widget(dashboard_id, widget_id)
    print('Dashboard Widget:')
    print(widget)
