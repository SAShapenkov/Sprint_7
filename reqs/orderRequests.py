import allure
import json
from reqs.baseRequests import BaseRequests
from constants import Constants


class OrderRequests(BaseRequests):

    @allure.step('Создаем заказ методом POST. Ожидаем статус респонса {status}')
    def create_order_post(self, data=None, status=201):
        url = Constants.ORDER_URL
        return self.post_request_and_check(url, data=json.dumps(data), status=status)

    @allure.step('Получаем список заказов методом GET. Ожидаем статус респонса {status}')
    def get_orders_list(self, status=200):
        url = Constants.ORDER_URL
        return self.get_request_and_check(url, status=status)
