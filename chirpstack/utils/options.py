import requests
import json

""" JWT временно хранится здесь, впоследствии - шлется в 
заголовке пользователем """
# jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjaGlycHN0YWNrLWFwcGxpY2F0aW9uLXNlcnZlciIsImV4cCI6MTU5NTk0MjQ3NiwiaWQiOjEsImlzcyI6ImNoaXJwc3RhY2stYXBwbGljYXRpb24tc2VydmVyIiwibmJmIjoxNTk1ODU2MDc2LCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.fWdI7mjhJw1i9WHYPzxfwyzYjFUEgyhd-jhL3Lvv4A4'


base_url = 'http://localhost:8080/'


def make_header(jwt: str):
    return {'Grpc-Metadata-Authorization': jwt,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Content-Encoding': 'ascii'}


def make_get(query: str, jwt: str) -> dict:
    res = requests.get(base_url + query, headers=make_header(jwt))
    return res.json()


def make_post(query, body: dict, jwt: str) -> dict:
    res = requests.post(base_url + query, headers=make_header(jwt), data=json.dumps(body))
    return res.json()


if __name__ == '__main__':
    pass
