# Faction Public APIs Python Client Examples

This directory contains several Python 3 scripts for Faction customers to execute in their account/environment.  These examples demonstrate how you can easily execute functionality using Faction Public APIs.  These are the same APIs we use in our portal.

## Getting Started

Before using the examples you will need to know several credentials which you will need to insert into the code.  Those credentials are as follows:

- Organization Id
- Client Id
- Client Secret

If you don't know any of these you can contact Faction support at [support@factioninc.com](support@factioninc.com) to get those values.

Once you gather this information you can fork the repo and start running the examples.

### Prerequisites 

#### Python

These examples have been tested with Python 3.9.x.   As a minimum it is required to have Python 3.7 or greater.

#### Setup Your Python Environment

The repo includes a **requirements.txt** in case you do not already have the listed packages installed.  It is assumed the user knows how to setup their Python environment using common tools such as pyenv or venv.

## Run The Examples

Currently there are examples to run:

- Create Fix Connection
- Get your CCVs
- Get Fix Connection

More information on request/response schemas of these examples can be found either in the **schema/openapi.yml** file in this repo or our online documentation found here [ https://api-docs-factioninc.com](https://api-docs-factioninc.com)

### Authentication

All of the examples need authentication.  Authentication is handled in the **auth.py** file. At the top of the file you will see this:

```python
TOKEN_URL = 'https://auth.factioninc.com/as/token'
CLIENT_ID = '<Your Client ID>'
CLIENT_SECRET = '<Your Client Secret>'
```

Add your respective client Id and secret

### Create FIX Connection

The **create_fix_connection.py** creates a FIX connection in AWS.  This file needs to be configured with your organization id. At the top of the file you will see this:

```python
FIX_CONNECTIONS_URL = 'https://api.factioninc.com/v2/fix/connections'
ORGANIZATION_ID = '<Your Organization ID>'
```

Add your organization Id

### Get CCV

The **get_ccv.py** returns a list of your ccvs.  This file needs to be configured with your organization id just like in the **create_fix_connection.py** file

### Get FIX Connections

The **get_fix_connections.py** returns a list of your FIX connections.  This file needs to be configured with your organization id just like in the **create_fix_connection.py** file