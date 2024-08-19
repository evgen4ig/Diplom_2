from data import Message
import helpers
import allure
from conftest import user


@allure.story('Тесты логина пользователей')
class TestUserLogin:
    @allure.title('Проверка успешной авторизации')
    def test_successful_user_login(self, user):
        response = helpers.login_user(user['email'], user['password'])
        assert response.status_code == 200

    @allure.title('Проверка авторизации с неверными email')
    def test_user_login_with_incorrect_email(self, user):
        response = helpers.login_user(helpers.generate_random_email(), user['password'])
        assert (response.status_code == 401 and
                response.json()['message'] == Message.EMAIL_OR_PASSWORD_INCORRECT_401)

    @allure.title('Проверка авторизации с неверными паролем')
    def test_user_login_with_incorrect_password(self, user):
        response = helpers.login_user(user['email'], helpers.generate_random_string())
        assert (response.status_code == 401 and
                response.json()['message'] == Message.EMAIL_OR_PASSWORD_INCORRECT_401)