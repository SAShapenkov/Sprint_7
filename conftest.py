import pytest
import allure
from faker import Faker

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
