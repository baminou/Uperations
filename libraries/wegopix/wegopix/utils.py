
import requests
import json

def login(host, email, password):
    data = {
        'email':email,
        'password': password
    }
    response = requests.post(_resolve(host,'/api/v1/login'),json.dumps(data),headers=_unauth_headers())
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()

def create_stream(host, token, name):
    data = {
        'name': name
    }
    return requests.post(_resolve(host,'/api/v1/streams'),json.dumps(data),headers=_auth_headers(token)).json()

def get_stream(host, token, alias):
    return requests.get(_resolve(host,'/api/v1/streams/'+alias),headers=_auth_headers(token))

def upload(host,marvel_host, token, stream_alias, upload_token,fp):
    data = {
        'upload_token': upload_token,
    }
    files = {'picture': fp}
    response = requests.post(_resolve(marvel_host,'/v1'),data,files=files,headers={'Accept':'application/json'})

    if response.status_code != 200:
        raise Exception(response.text)

    data = response.json()
    data['upload_token'] = data.get('upload_token').get('id')

    response = requests.post(_resolve(host,'/api/v1/streams/'+stream_alias+'/pictures'),json.dumps(data),headers=_auth_headers(token))

    if response.status_code != 201:
        raise Exception(response.text)

    return response.json()

def _auth_headers(token):
    headers = _unauth_headers()
    headers['Authorization'] = 'Bearer '+token
    return headers

def _unauth_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def _resolve(host, endpoint):
    return host+endpoint