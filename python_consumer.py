from importlib.metadata import requires
import requests

root = 'http://localhost:8000/'
path = 'auth/jwt/create/'
endpoint = root + path
username = 'admin'
password = 'lol14112003'
data = {
    'username':username,
    'password':password,
}
response = requests.post(endpoint,json=data)
access_token = response.json()['access']

path = 'social/posts/'
endpoint = root + path
header_type = "JWT"
headers = {
    "Authorization": f"{header_type} {access_token}"
}

data = {
    'title' :'new title',
    'body': 'new content'
}
response = requests.post(endpoint,headers=headers,json=data)
print(response)