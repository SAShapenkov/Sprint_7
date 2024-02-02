import allure
from reqs.courierRequests import CourierRequests
import pytest
import json


@allure.feature('Проверка регистрации курьеров')
class TestCourierRegister:

    @allure.title('Успещная регистрация курьера')
    def test_registration_login(self, create_courier_login_and_delete):
        response = create_courier_login_and_delete
        assert response['ok']

    @allure.title('Проверка ошибки пои создании двух курьеров с одинаковыми логинами')
    def test_create_existing_courier_login(self, create_user_payload):
        crr = CourierRequests()
        payload = create_user_payload
        crr.create_courier_post(payload)
        response = crr.login_courier_post(payload)
        response_double = crr.create_courier_post(payload, status=409)
        courier_id = response["id"]
        crr.delete_courier(courier_id=courier_id)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("payload_data",
                             [
                                 ['', '1234', 'Alex'],
                                 ['buba', '', 'Nick'],
                                 ['', '', 'Joe'],
                                 ['', '1234', ''],
                                 ['rrudy', '', '']
                             ])
    @allure.title('Проверка что без обязательных данных (логин, пароль) курьер не создается')
    def test_required_fields_on_register(self, payload_data):
        crr = CourierRequests()
        payload = json.dumps(payload_data)
        response = crr.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
