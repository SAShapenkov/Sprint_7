import pytest
import allure

from reqs.orderRequests import OrderRequests

@allure.feature('Проверка создания и выгрузки списка заказов')
class TestOrderOperations:
    @allure.description('Проверка возможности заказать с разынми цветами, ответ содержит "track"')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None])
    def test_create_order_successful(self, color, create_order_payload):
        orr = OrderRequests()
        payload = create_order_payload
        response = orr.create_order_post(payload)
        assert "track" in response.keys()

    @allure.description('Ручка возвращает список заказов')
    def test_get_order_returns_list(self):
        orr = OrderRequests()
        response = orr.get_orders_list()
        assert "orders" in response.keys()