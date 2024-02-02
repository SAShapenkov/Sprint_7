import allure
from reqs.courierRequests import CourierRequests
import pytest
import json

@allure.feature('Проверка авторизации курьеров')
class TestCourierLogin:
    @allure.title('Успешный вход зарегистрированного курьера')
    def test_login(self):
        crr = CourierRequests()
        payload = crr.create_user_payload()
        crr.create_courier_post(payload)
        response = crr.login_courier_post(payload)
        assert response.get('id') is not None

    @pytest.mark.parametrize("login, password",
                             [
                                 ('Jason Arnold', ''),
                                 ('', '1234'),
                             ]
                             )
    @allure.title('Проверка что без одного обязательного поля (логин или пароль) курьер не входит')
    def test_required_fields_on_login(self, login, password):
        crr = CourierRequests()
        payload = crr.create_login_payload(login, password)
        response = crr.login_courier_post(payload, status=400)
        assert response['message'] == 'Недостаточно данных для входа'


    @allure.title('Зарегистрированный курьер не может войти с неверным паролем')
    def test_login(self):
        crr = CourierRequests()
        payload = crr.create_login_payload('Jason Arnold', '12345')
        response = crr.login_courier_post(payload, status=404)
        assert response['message'] == 'Учетная запись не найдена'

    @allure.title('Курьер, сначала созаднный а потом удаленный, не может войти в систему')
    def test_courier_cant_login_after_deleting_account(self):
        crr = CourierRequests()
        payload = crr.create_user_payload()
        crr.create_courier_post(payload)
        response = crr.login_courier_post(payload)
        courier_id = response["id"]
        response_delete = crr.delete_courier(courier_id=courier_id)
        assert response_delete['ok']
        response = crr.login_courier_post(payload, status=404)
        assert response["message"] == "Учетная запись не найдена"