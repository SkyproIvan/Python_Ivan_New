import pytest
import requests


base_url = "https://ru.yougile.com/api-v2/"

def test_add_token():

    token = {
        "login": "skypro_ivan@mail.ru",
        "password": "Zreijdrf_2013",
        "companyId": "c13fdb15-670c-4a71-a234-3cf0a8f8eed3"
        }
    auth = requests.post(base_url + 'auth/keys', json=token)
    assert auth.status_code == 201
    return auth.json()["key"]


key = "1XiuI9dKA1j0WOjXkfmpilV25Y1F+XkxG3D8yZiVkLB29Kj2kE5bQdXOpQONFR66"
headers = {"Authorization": f"Bearer {key}"}


def test_POST():

    POST_body = {
        "title": "Мой второй проект"
        }
    first_project = requests.post(base_url + 'projects', json=POST_body, headers=headers)
    assert first_project.status_code == 201
    print(first_project.json())



def test_PUT():
    id_for_project_1 = "1932bd10-d25d-4e0e-95d0-2999672570fb"
    PUT_body_new = {
        "title": "Мой гениальный проект, заслуживающий внимания3"
    }
    genius_project = requests.put(base_url + 'projects/id_for_project_1', json=PUT_body_new, headers=headers)
    assert id_for_project_1 == "1932bd10-d25d-4e0e-95d0-2999672570fb"
    assert genius_project.status_code == 200

    print(genius_project.json())



def test_GET():
    so_get_my_project = requests.get(base_url + 'projects/id_for_project_1', headers=headers)
    assert so_get_my_project.status_code == 200
