import json
import unittest
from main import app
from util.dbconection import db
from models.products import Products
import os 


class OrdersTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)
        self.db = db
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer mock_token_aJJSVxxx"}

        os.system('python setup/init_db.py')
        

    def test_list_orders(self):
        response = self.app.get('/orders/', headers=self.headers)
        self.assertEqual(200, response.status_code)

    def test_list_orders_by_product(self):
        response = self.app.get('/orders/?product_id=1', headers=self.headers)
        self.assertEqual(response.get_json()["product_id"], "1")
        self.assertEqual(200, response.status_code)

    def test_order_get(self):
        response = self.app.get('/orders/1', headers=self.headers)
        self.assertEqual(200, response.status_code)

    def test_order_delete(self):
        response = self.app.delete(
            '/orders/1', headers=self.headers)
        self.assertEqual(response.get_json()["message"], "success")
        self.assertEqual(200, response.status_code)

    def test_order_update(self):
        payload = json.dumps({
            "actual_price": 200,
        })
        response = self.app.put(
            '/orders/2', headers=self.headers,  data=payload)
        self.assertEqual(response.get_json()["message"], "success",)
        self.assertEqual(200, response.status_code)

    def test_order_post_1(self):
        payload = json.dumps({
            "product_id": 99999999999999,
            "actual_price": 200,
        })
        response = self.app.post(
            '/orders/', headers=self.headers,  data=payload)
        self.assertEqual(response.get_json()[
                         "message"], "Product is not found",)
        self.assertEqual(200, response.status_code)

    def test_order_post_2(self):
        # Fetching any product
        product = Products.query.first()
        payload = json.dumps({
            "product_id": product.id,
            "actual_price": 200,
        })
        response = self.app.post(
            '/orders/', headers=self.headers,  data=payload)
        self.assertEqual(response.get_json()["message"], "success",)
        self.assertEqual(200, response.status_code)

    def test_order_metrics(self):
        response = self.app.get('/orders/metrics', headers=self.headers)
        self.assertEqual(response.get_json()["message"], "success",)
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        self.db.session.remove()
        self.db.engine.dispose()


if __name__ == '__main__':
    unittest.main()
    app.run()
