import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME, UPDATED_USER_SCHEME
import datetime

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"
UPDATE_USER_BY_ID = 'api/users/2'

def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    assert response.status_code == 201
    assert creation_date[0:16] == current_date[0:16]  # указываем количество символов, до которых берём значение
    assert response_json['name'] == body['name']  # сравниваем, что полученный json совпадает с тем, что указан в body
    assert response_json['job'] == body['job']

def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    assert response.status_code == 201
    assert creation_date[0:16] == current_date[0:16] # указываем количество символов, до которых берём значение
    assert response_json['job'] == body['job']

def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    response_json = response.json()
    creation_date = response_json['createdAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    assert response.status_code == 201
    assert creation_date[0:16] == current_date[0:16]  # указываем количество символов, до которых берём значение
    assert response_json['name'] == body['name']  #сравниваем, что полученный json совпадает с тем, что указан в body


#запросы с put
def test_update_user_by_id_by_put():
#предполагаю, что даже при отправке в теле одного из ключей, в ответ вернутся все ключи из схемы
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']

def test_update_user_by_id_without_job_by_put():
    body = {
        "name": "morpheus"
    }
    response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['name'] == body['name']

def test_update_user_by_id_without_name_by_put():
    body = {
        "job": "zion resident"
    }
    response = httpx.put(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['job'] == body['job']

#запросы с patch
def test_update_user_by_id_by_patch():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']

def test_update_user_by_id_without_job_by_patch():
    body = {
        "name": "morpheus"
    }
    response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['name'] == body['name']

def test_update_user_by_id_without_name_by_patch():
    body = {
        "job": "zion resident"
    }
    response = httpx.patch(BASE_URL + UPDATE_USER_BY_ID, json=body)
    response_json = response.json()
    creation_date = response_json['updatedAt'].replace("T", " ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    assert response.status_code == 200
    assert creation_date[0:16] == current_date[0:16]
    assert response_json['job'] == body['job']

#удаление юзера
def test_delete_user_by_id():
        responce = httpx.delete(BASE_URL + UPDATE_USER_BY_ID)
        assert responce.status_code == 204