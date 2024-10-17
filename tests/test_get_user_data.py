import httpx
from jsonschema import validate
from  core.contracts import RESOURCE_DATA_SCHEME, USER_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/" # Основной URL
LIST_RESOURCE = "api/unknown"
COLOR_START = "#"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"



LIST_USERS = "api/users?page=2" # Endpoint
SINGLE_USER = "api/users/2"
EMAIL_ENDS = "@reqres.in"
NOT_FOUND_USER = "api/users/23"
AVATAR_ENDS = "-image.jpg"

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200


    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание Email адреса'):
                assert item['email'].endswith(EMAIL_ENDS) # проверяем, что `mail заканчивается на @reqres.in
            with allure.step('Проверяем наличие id в ссылке на аватарку'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS) # проверяем, что в конце верный аватар

@allure.suite('Проверка запроса одного пользователя')
@allure.title('Проверяем получение одного пользователя по id')
def test_single_user():
    with allure.step(f'Проверяем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем окончание Email адреса'):
        assert data['email'].endswith(EMAIL_ENDS)  # проверяем, что `mail заканчивается на @reqres.in
    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)  # проверяем, что в конце верный аватар

def test_user_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_USER)
    assert  response.status_code == 404

def test_list_resource():
    responce = httpx.get(BASE_URL + LIST_RESOURCE)
    assert responce.status_code == 200
    data = responce.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)
        assert item['color'].startswith(COLOR_START) # проверяем, что значение цвета начинается с решетки

def test_single_resource():
    responce = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert responce.status_code == 200
    data = responce.json()['data']

    assert data['color'].startswith(COLOR_START)  # проверяем, что значение цвета начинается с решетки

def test_single_resource_not_found():
    responce = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    assert responce.status_code == 404
