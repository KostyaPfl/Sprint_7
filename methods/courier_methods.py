import allure

from urls import BASE_URL, COURIERS_URL
import requests
from helpers import generate_random_string


class CourierMethods:
    @allure.step('Генерируем данные для регистрации курьера')
    def courier_data_generation(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        return {
            "login": login,
            "password": password,
            "first_name": first_name
        }

    @allure.step('Регистрируем нового курьера')
    def registration_new_courier(self, payload):
        return requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)

    @allure.step('Логинимся курьером')
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data=payload)

    @allure.step('Удаляем курьера из системы')
    def delete_courier(self, courier_id):
        return requests.delete(f'{BASE_URL}{COURIERS_URL}/{courier_id}')
