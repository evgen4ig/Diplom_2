import allure
from conftest import *
import helpers
from data import TestData, Message


@allure.story('Тесты создания заказов')
class TestOrderCreating:
    @allure.title('Проверка создания заказа с авторизацией')
    def test_order_creating_with_authorization(self, user):
        response = helpers.create_order(TestData.INGREDIENT, user['json']['accessToken'])
        assert response.status_code == 200 and response.json()['order']['owner']['email'] == user['email']

    @allure.title('Проверка создания заказа')
    def test_order_creating(self):
        response = helpers.create_order(TestData.INGREDIENT)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без ингридиента')
    def test_order_creating_without_ingredient(self):
        response = helpers.create_order()
        assert (response.status_code == 400 and
                response.json()['message'] == Message.INGREDIENTS_MUST_BE_PROVIDED_400)

    @allure.title('Проверка создания заказа с неверным хэшем')
    def test_order_creating_with_incorrect_hash(self):
        response = helpers.create_order('мэш')
        assert response.status_code == 500