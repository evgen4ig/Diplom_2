import requests
import allure
import random
import string

from data import Url


@allure.step('Генерируем рандомную строку')
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерируем рандомный email')
def generate_random_email():
    return f'{generate_random_string()}@gmail.com'


@allure.step('Регистрируем нового пользователя и возвращаем его данные')
def register_new_user_and_return_user_data():

    user_data = {}

    email = generate_random_email()
    password = generate_random_string()
    name = generate_random_string()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(Url.BASE_URL+Url.CREATE_USER_HANDLE, data=payload)

    if response.status_code == 200:
        user_data = {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': response.json()
        }

    return user_data


@allure.step('Удаляем пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.BASE_URL+Url.DELETE_USER_HANDLE, headers=headers)


@allure.step('Авторизуем пользователя')
def login_user(email, password):
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(Url.BASE_URL+Url.LOGIN_USER_HANDLE, data=payload)
    return response


@allure.step('Создаем заказ')
def create_order(ingredient=None, access_token=None):
    payload = {
        'ingredients': [ingredient]
    }
    headers = {'Authorization': access_token}
    response = requests.post(Url.BASE_URL+Url.ORDERS_HANDLE, data=payload, headers=headers)
    return response


@allure.step('Получаем список заказов')
def get_user_orders(access_token=None):
    headers = {'Authorization': access_token}
    response = requests.get(Url.BASE_URL+Url.ORDERS_HANDLE, headers=headers)
    return response