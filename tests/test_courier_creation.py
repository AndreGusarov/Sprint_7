import allure
import requests
from handle import Handle
from url import Url
from generator import register_new_courier
from generator import register_new_courier_without_login as courier_without_login
from generator import register_new_courier_without_password as courier_without_psw

class TestCreateCourier:
    data = register_new_courier()

    @allure.title('Создание курьера')
    def test_courier_creation(self):
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Url.URL}{Handle.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier_creation(self):
        response = requests.post(
            f'{Url.URL}{Handle.CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text 
        
    @allure.title('Проверка, что нельзя создать курьера без логина')
    def test_courier_without_login_creation(self):
        response = requests.post(
            f'{Url.URL}{Handle.CREATE_COURIER}',
            courier_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Проверка, что нельзя создать курьера без пароля')
    def test_courier_without_password_creation(self):
        response = requests.post(
            f'{Url.URL}{Handle.CREATE_COURIER}',
            courier_without_psw())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text