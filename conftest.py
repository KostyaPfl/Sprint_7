import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier():
    payload = CourierMethods().courier_data_generation()
    creation_response = CourierMethods().registration_new_courier(payload)
    login = payload['login']
    password = payload['password']
    courier_id = CourierMethods().login_courier(login, password).json()['id']
    yield courier_id, payload, creation_response
    CourierMethods().delete_courier(courier_id)


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def order_methods():
    return OrderMethods()
