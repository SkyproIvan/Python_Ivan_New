import pytest
import requests

base_url = "https://ru.yougile.com/api-v2/projects"


def test_add_token():
    token = {
        "login": "...@mail.ru",
        "password": "...",
        "companyId": "c13fdb15-670c-4a71-a234-3cf0a8f8eed3"
    }
    auth = requests.post(base_url + 'auth/keys', json=token)
    assert auth.status_code == 201
    return auth.json()["key"]


key = "1XiuI9dKA1j0WOjXkfmpilV25Y1F+XkxG3D8yZiVkLB29Kj2kE5bQdXOpQONFR66"
headers = {"Authorization": f"Bearer {key}"}


@pytest.fixture(scope="module")
def created_project_id():
    POST_body = {"title": "Мой второй проект"}
    response = requests.post(base_url, json=POST_body, headers=headers)

    # Проверяем, что проект создался успешно
    assert response.status_code == 201

    # Извлекаем ID из ответа и возвращаем его
    project_data = response.json()
    return project_data.get('id')


@pytest.mark.positive
def test_POST():
    POST_body = {
        "title": "Мой второй проект"
    }
    first_project = requests.post(base_url, json=POST_body, headers=headers)
    assert first_project.status_code == 201
    print(first_project.json())
    created_project_id1 = first_project.json().get('id')
    print(created_project_id1)


@pytest.mark.positive
def test_PUT(created_project_id):
    project_id = created_project_id
    PUT_body_new = dict(title="Мой гениальный проект, заслуживающий внимания3")
    genius_project = requests.put(f"{base_url}/{project_id}", json=PUT_body_new, headers=headers)
    assert genius_project.status_code == 200
    print(PUT_body_new)
    print(genius_project.json())


@pytest.mark.positive

def test_GET():
    project_id = "f7261e07-0d27-40bb-897a-fd3cba820711"
    so_get_my_project = requests.get(f"{base_url}/{project_id}", headers=headers)
    assert so_get_my_project.status_code == 200
    print(so_get_my_project.json())


# в переменной base_url2 допустим ошибку project вместо projects


base_url2 = "https://ru.yougile.com/api-v2/project"


@pytest.mark.negative

def test_POST_negative():
    POST_body = dict(title="Мой второй проект")
    # в переменной base_url допустим ошибку project вместо projects в присвоении в верхней части кода
    first_project = requests.post(base_url2, json=POST_body, headers=headers)
    assert first_project.status_code == 404
    print(first_project.json())
    created_project_id1 = first_project.json().get('id')
    print(created_project_id1)


@pytest.mark.negative
def test_PUT_negative(created_project_id):
    project_id = created_project_id
    PUT_body_new = {
        "title": "Мой гениальный проект, заслуживающий внимания3"
    }
    genius_project = requests.put(f"{base_url2}/{project_id}", json=PUT_body_new, headers=headers)
    assert genius_project.status_code == 404
    print(genius_project.json())


@pytest.mark.negative
def test_GET_negative():
    project_id = "f7261e07-0d27-40bb-897a-fd3cba820711"
    so_get_my_project = requests.get(f"{base_url2}/{project_id}", headers=headers)
    assert so_get_my_project.status_code == 404
