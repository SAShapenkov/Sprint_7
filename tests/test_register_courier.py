import allure
from reqs.courierRequests import CourierRequests
import pytest
import json


@allure.feature('Проверка регистрации курьеров')
class TestCourierRegister:
    @allure.description('Успещная регистрация курьера')
    def test_registration_login(self):
        crr = CourierRequests()
        response = crr.create_courier_post(crr.create_user_payload())
        assert response['ok']

    @allure.description('Проверка ошибкт пои создании двух курьеров с одинаковыми логинами')
    def test_create_existing_courier_login(self):
        crr = CourierRequests()
        payload = crr.create_user_payload()
        crr.create_courier_post(payload)
        response_double = crr.create_courier_post(payload, status=409)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("payload_data",
                             [
                                 ['', '1234', 'Alex'],
                                 ['buba', '', 'Nick'],
                                 ['', '', 'Joe'],
                                 ['', '1234', ''],
                                 ['rrudy', '', '']
                             ])
    @allure.description('Проверка что без обязательных данных (логин, пароль) курьер не создается')
    def test_required_fields_on_register(self, payload_data):
        crr = CourierRequests()
        payload = json.dumps(payload_data)
        response = crr.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
