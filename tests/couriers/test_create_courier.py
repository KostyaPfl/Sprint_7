import allure
import pytest


class TestCreateCourier:

    @allure.title('Проверяем регистрацию нового курьера, успешный запрос возвращает "ok":true, статус ответа 201')
    def test_create_courier(self, courier):
        response = courier[2]
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверяем, что нельзя зарегистрировать двух одинаковых курьеров. Возвращается сообщение об ошибке, '
                  'статус ответа 409')
    def test_create_two_identical_couriers(self, courier_methods, courier):
        payload = courier[1]
        response = courier_methods.registration_new_courier(payload)
        assert (response.status_code == 409
                and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Проверяем что нельза зарегистрировать курьера при отсутствии обязательных полей логина или пароля. '
                  'Возвращается сообщение об ошибке, статус ответа 400')
    @pytest.mark.parametrize(
        'empty_field_name',
        ["login", "password"]
    )
    def test_create_courier_with_empty_field_login_or_password(self, courier_methods, empty_field_name):
        payload = courier_methods.courier_data_generation()
        payload[empty_field_name] = ''
        response = courier_methods.registration_new_courier(payload)
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверяем что возможно зарегистрировать курьера при отсутствии поля first_name, запрос возвращает '
                  '"ok":true, статус ответа 201')
    def test_create_courier_with_empty_field_first_name(self, courier_methods):
        payload = courier_methods.courier_data_generation()
        payload['first_name'] = ''
        response = courier_methods.registration_new_courier(payload)
        courier_id = courier_methods.login_courier(payload['login'], payload['password'])
        courier_methods.delete_courier(courier_id)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    