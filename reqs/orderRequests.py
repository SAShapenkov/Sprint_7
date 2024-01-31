import allure
import json
from reqs.baseRequests import BaseRequests


class OrderRequests(BaseRequests):
    order_handler = '/api/v1/orders'

    @allure.step('Создаем заказ методом POST. Ожидаем статус респонса {status}')
    def create_order_post(self, data=None, status=201):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
        return self.post_request_and_check(url, data=json.dumps(data), status=status)

    @allure.step('Получаем список заказов методом GET. Ожидаем статус респонса {status}')
    def get_orders_list(self, status=200):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
        return self.get_request_and_check(url, status=status)
