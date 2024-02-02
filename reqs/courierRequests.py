import allure
from reqs.baseRequests import BaseRequests
from faker import Faker
import json
from constants import Constants

fake = Faker()


class CourierRequests(BaseRequests):

    @allure.step('Создаем курьера методом POST. Ожидаем статус респонса {status}')
    def create_courier_post(self, data=None, status=201):
        url = Constants.COURIER_URL
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Логиним курьера методом POST. Ожидаем статус респонса {status}')
    def login_courier_post(self, data=None, status=200):
        url = Constants.COURIER_LOGIN_URL
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Удаляем курьера методом DELETE. Ожидаем статус респонса {status}')
    def delete_courier(self, data=None, courier_id=None, status=200):
        url = f'{Constants.COURIER_URL}{courier_id}'
        return self.delete_request_and_check(url, data=data, status=status)

    def create_user_payload(self):
        data = {
            "firstName": fake.name(),
            "login": fake.name(),
            "password": fake.pyint()
        }
        return json.dumps(data)

    def create_login_payload(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        return json.dumps(data)
