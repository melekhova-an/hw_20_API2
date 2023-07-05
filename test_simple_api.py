import requests
from jsonschema.validators import validate

from helper import load_json_schema



def test_post_successful_loin():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'
    schema = load_json_schema('post_successful_loin.json')
    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            'email': email,
            'password': password
        })

    validate(instance=response.json(), schema=schema)


def test_post_successful_register():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            'email': email,
            'password': password
        })
    schema = load_json_schema('post_successful_register.json')
    validate(instance=response.json(), schema=schema)


def test_put_update_user():
    name = 'An'
    job = 'student'

    response = requests.put(
        url='https://reqres.in/api/users/2',
        json={
            'name': name,
            'job': job
        }
    )
    schema = load_json_schema('put_update_user.json')
    validate(instance=response.json(), schema=schema)


def test_patch_update_user():
    name = 'An'
    job = 'student'

    response = requests.patch(
        url='https://reqres.in/api/users/2',
        json={
            'name': name,
            'job': job
        }
    )

    schema = load_json_schema('patch_update_user.json')
    validate(instance=response.json(), schema=schema)


def test_post_create_user():
    name = 'An'
    job = 'student'

    response = requests.post(
        url='https://reqres.in/api/users',
        json={
            'name': name,
            'job': job
        }
    )
    schema = load_json_schema('post_create_user.json')
    validate(instance=response.json(), schema=schema)


def test_get_unknown_users():

    response = requests.get('https://reqres.in/api/unknown')
    schema = load_json_schema('get_unknown_users.json')
    validate(instance=response.json(), schema=schema)


def test_get_single_users():

    response = requests.get('https://reqres.in/api/users/2')
    schema = load_json_schema('get_single_users.json')
    validate(instance=response.json(), schema=schema)


def test_get_single_unknown():

    response = requests.get('https://reqres.in/api/unknown/2')
    schema = load_json_schema('get_single_unknown.json')
    validate(instance=response.json(), schema=schema)


def test_post_unsuccessful_loin():

    response = requests.post('https://reqres.in/api/login')
    schema = load_json_schema('post_unsuccessful_loin.json')
    validate(instance=response.json(), schema=schema)


def test_post_unsuccessful_register():

    response = requests.post('https://reqres.in/api/register')
    schema = load_json_schema('post_unsuccessful_register.json')
    validate(instance=response.json(), schema=schema)