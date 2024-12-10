import allure


class TestGetOrdersList:
    @allure.title('Проверяем что в ответе приходит список заказов, статус ответа 200')
    def test_get_orders_list(self, order_methods):
        response = order_methods.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()
