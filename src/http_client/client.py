import pprint

import requests


#  request & response

def http_client_get(user_id):
    headers = {
        "Content-Type": "application/json"
    }

    url = f'http://localhost:3000/user-management/{user_id}'

    response = requests.get(url=url, headers=headers)

    pprint.pprint(response.json())


def http_client_post():
    headers = {
        "Content-Type": "application/json"
    }

    url = 'http://localhost:3000/user-management/add'

    request = {
        "userName": "charlie",
        "password": "pedroEsMarico",
        "email": "charlie@charlie.com",
        "userType": "admin"
    }

    response = requests.post(url=url, headers=headers, json=request)

    print(response.text)


def http_client_delete(user_id):
    url = f'http://localhost:3000/user-management/delete/{user_id}'

    response = requests.put(url=url)

    print(response.text)


if __name__ == '__main__':
    # http_client_post()
    http_client_get("3")
    # http_client_delete("3")
