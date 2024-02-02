import pytest
import allure
import json
from faker import Faker
from reqs.courierRequests import CourierRequests

faker = Faker()

@pytest.fixture
@allure.step('Конструируем запрос для отправки заказа')
def create_order_payload():
    fake_date = faker.date_between(start_date='today', end_date='+1y')
    date = fake_date.strftime("%Y-%m-%d")
    payload = {"firstName": faker.first_name(), "lastName": faker.last_name(),
               "address": faker.address(), "metroStation": 1, "phone": "+76665551122", "rentTime": 2,
               "deliveryDate": date,
               "comment": "Ненавижу самокаты"}
    return payload

@pytest.fixture
@allure.step('Создание курьера, логин и удаление')
def create_courier_login_and_delete(create_user_payload):
    payload = create_user_payload
    CourierRequests.create_courier_post(payload)
    response = CourierRequests.login_courier_post(payload)
    return response
    CourierRequests.delete_courier(courier_id=response["id"])

@pytest.fixture
@allure.step('Создание данных курьера')
def create_user_payload():
    data = {
        "firstName": faker.name(),
        "login": faker.name(),
        "password": faker.pyint()
        }
    return json.dumps(data)