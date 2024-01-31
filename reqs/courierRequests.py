import allure
from reqs.baseRequests import BaseRequests
from faker import Faker
import json
fake = Faker()

class CourierRequests(BaseRequests):

    @allure.step('Создаем курьера методом POST. Ожидаем статус респонса {status}')
    def create_courier_post(self, data=None, status=201):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Логиним курьера методом POST. Ожидаем статус респонса {status}')
    def login_courier_post(self, data=None, status=200):
        url = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Удаляем курьера методом DELETE. Ожидаем статус респонса {status}')
    def delete_courier(self, data=None, courier_id=None, status=200):
        url = f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
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



