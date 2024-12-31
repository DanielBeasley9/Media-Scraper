import requests

CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'

response = requests.post(
    'https://id.twitch.tv/oauth2/token',
    params={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
)

data = response.json()
access_token = data['access_token']
print(f"Access Token: {access_token}")