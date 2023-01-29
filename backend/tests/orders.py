import unittest
from main import app
from util.dbconection import db


class OrdersTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer mock_token_aJJSVxxx"}

    def test_list_orders(self):
        response = self.app.get('/orders/', headers=self.headers)
        self.assertEqual(200, response.status_code)

    def test_order_get(self):
        response = self.app.get('/orders/1', headers=self.headers)
        self.assertEqual(200, response.status_code)

    def test_order_delete(self):
        response = self.app.delete(
            '/orders/1', headers=self.headers)
        self.assertEqual(response.get_json()["message"], "success")
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
    app.run()