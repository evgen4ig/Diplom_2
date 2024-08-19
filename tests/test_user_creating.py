import pytest
import requests
import allure
import helpers
from data import Url, Message
from conftest import *

@allure.story('Тесты создания пользователей')
class TestUserCreating:
    @allure.title('Проверка успешного создания пользователя')
    def test_successful_user_creating(self, user):
        assert user['status_code'] == 200

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_user_creating_using_same_data(self, user):
        payload = {
            'email': user['email'],
            'password': user['password'],
            'name': user['name']
        }
        response = requests.post(Url.BASE_URL+Url.CREATE_USER_HANDLE, data=payload)
        assert (response.status_code == 403 and
                response.json()['message'] == Message.USER_ALREADY_EXIST_403)

    @allure.title('Проверка создания пользователя без заполнения одного из обязательных полей')
    @pytest.mark.parametrize('td_email, td_password, td_name',
                             [['', helpers.generate_random_string(), helpers.generate_random_string()],
                              [helpers.generate_random_email(), '', helpers.generate_random_string()],
                              [helpers.generate_random_email(), helpers.generate_random_string(), '']])
    def test_user_creating_with_empty_field(self, td_email, td_password, td_name):
        payload = {
            'email': td_email,
            'password': td_password,
            'name': td_name
        }
        response = requests.post(Url.BASE_URL+Url.CREATE_USER_HANDLE, data=payload)
        assert (response.status_code == 403
                and response.json()['message'] == Message.REQUIRED_FIELD_EMPTY_403)