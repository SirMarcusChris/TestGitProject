import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME, LOGIN_USER_SCHEME
import allure

BASE_URL = "https://reqres.in/"
REGISTERED_USER = "api/register"
LOGIN_USER = "api/login"
json_file = open('./core/new_users_data.json')
users_data = json.load(json_file)


@allure.suite('Проверка возможности создания пользователя методом post параметризированным тестом')
@allure.title('Проверяем создание пользователя')
@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    response = httpx.post(BASE_URL + REGISTERED_USER, json=users_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверяем элементы из списка по схеме'):
        validate(response.json(), REGISTERED_USER_SCHEME)

@allure.suite('Проверка успешного входа пользователя методом post параметризированным тестом')
@allure.title('Проверяем создание пользователя')
@pytest.mark.parametrize('users_data', users_data)
def test_successful_registered(users_data):
    response = httpx.post(BASE_URL + LOGIN_USER,json=users_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверяем элементы из списка по схеме'):
        validate(response.json(), LOGIN_USER_SCHEME)








