import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME, UPDATED_USER_SCHEME
import datetime
import allure


BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"
UPDATE_USER_BY_ID = 'api/users/2'

@allure.suite('Проверка возможности создания пользователя методом post')
@allure.title('Проверяем создание пользователя')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step('Проверяем элемент из списка по схеме'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    with allure.step('Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16] #указываем количество символов, до которых берём значение
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name'] #сравниваем,что полученный json совпадает с тем, что указан в body
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности создания пользователя методом post без указания name')
@allure.title('Проверяем создание пользователя')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step('Проверяем элемент из списка по схеме'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    with allure.step('Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16] # указываем количество символов, до которых берём значение
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности создания пользователя методом post без указания job')
@allure.title('Проверяем создание пользователя')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]#указываем количество символов, до которых берём значение
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name']#сравниваем, что полученный json совпадает с тем, что указан в body


#запросы с put
@allure.suite('Проверка возможности создания пользователя методом put')
@allure.title('Проверяем создание пользователя')
def test_update_user_by_id_by_put():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности создания пользователя методом put без указания job')
@allure.title('Проверяем создание пользователя')
def test_update_user_by_id_without_job_by_put():
    body = {
        "name": "morpheus"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name']


@allure.suite('Проверка возможности создания пользователя методом put без указания name')
@allure.title('Проверяем создание пользователя')
def test_update_user_by_id_without_name_by_put():
    body = {
        "job": "zion resident"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности создания пользователя методом patch')
@allure.title('Проверяем создание пользователя')
#запросы с patch
def test_update_user_by_id_by_patch():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name']
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности создания пользователя методом patch без указания job')
@allure.title('Проверяем создание пользователя')
def test_update_user_by_id_without_job_by_patch():
    body = {
        "name": "morpheus"
    }
    with allure.step('Отправка запроса с телом на создание пользователя'):
        response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step(f'Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения имени у созданного пользователя с указанным'):
        assert response_json['name'] == body['name']


@allure.suite('Проверка возможности создания пользователя методом patch без указания name')
@allure.title('Проверяем создание пользователя')
def test_update_user_by_id_without_name_by_patch():
    body = {
        "job": "zion resident"
    }
    with allure.step('Проверяем элемент из списка по схеме'):
        response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step(f'Проверяем элемент из списка по схеме'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    with allure.step('Проверка совпадения времени создания пользователя с текущим временем'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step('Проверка совпадения работы у созданного пользователя с указанным'):
        assert response_json['job'] == body['job']


@allure.suite('Проверка возможности удаления пользователя')
@allure.title('Проверяем удаление пользователя')
def test_delete_user_by_id():
    with allure.step('Отправка запроса на удаление пользователя'):
        responce = httpx.delete(BASE_URL + UPDATE_USER_BY_ID)
    with allure.step('Проверяем код ответа'):
        assert responce.status_code == 204