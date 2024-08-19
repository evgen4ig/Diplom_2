import allure
import requests
from conftest import *
import helpers
from data import TestData, Message


@allure.story('Тесты получения заказов пользователя')
class TestGetUserOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_orders_authorized_user(self, user):
        helpers.create_order(TestData.INGREDIENT, user['json']['accessToken'])
        response = helpers.get_user_orders(user['json']['accessToken'])
        assert (response.status_code == 200 and
                (TestData.INGREDIENT in order['ingredients'] for order in response.json()['orders']))

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_orders_non_authorized_user(self):
        helpers.create_order(TestData.INGREDIENT)
        response = helpers.get_user_orders()
        assert (response.status_code == 401 and
                response.json()['message'] == Message.SHOULD_BE_AUTHORISED_401)