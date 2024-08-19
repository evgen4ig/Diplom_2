import allure
import pytest
import requests
from conftest import *
import helpers
from data import Url, Message


@allure.story('Тесты изменения данных пользователя')
class TestUserDataEdit:
    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('test_data', ['email', 'name'])
    def test_authorized_user_data_edit(self, user, test_data):
        if test_data == 'email':
            payload = {
                test_data: helpers.generate_random_email()
            }
        else:
            payload = {
                test_data: helpers.generate_random_string()
            }
        response = requests.patch(Url.BASE_URL+Url.EDIT_USER_HANDLE, data=payload,
                                  headers={'Authorization': f'{user["json"]["accessToken"]}'})
        assert (response.status_code == 200 and
                response.json()['user'][test_data] == payload[test_data])

    @allure.title('Проверка изменения emaila на уже используемый')
    def test_authorized_user_change_email_on_used(self, user):
        new_user = helpers.register_new_user_and_return_user_data()
        payload = {
            'email': user['email']
        }
        response = requests.patch(Url.BASE_URL+Url.EDIT_USER_HANDLE, data=payload,
                                  headers={'Authorization': f'{new_user["json"]["accessToken"]}'})
        helpers.delete_user(new_user['json']['accessToken'])
        assert (response.status_code == 403 and
                response.json()['message'] == Message.EMAIL_ALREADY_EXIST_403)

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('test_data', ['email', 'name'])
    def test_non_authorized_user_data_edit(self, user, test_data):
        if test_data == 'email':
            payload = {
                test_data: helpers.generate_random_email()
            }
        else:
            payload = {
                test_data: helpers.generate_random_string()
            }
        response = requests.patch(Url.BASE_URL+Url.EDIT_USER_HANDLE, data=payload)
        assert (response.status_code == 401 and
                response.json()['message'] == Message.SHOULD_BE_AUTHORISED_401)