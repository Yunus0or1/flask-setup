from flask import Blueprint
from middlewares.jwt_token_middleware import jwt_token_middleware
from models.orders import Orders
from models.products import Products

orders_pages = Blueprint('orders', __name__, url_prefix='/orders')


@orders_pages.route('/', methods=['GET'])
@jwt_token_middleware
def list_orders():
    print(Products.query.all())
    return '<h3>Test</h3>'
    pass


@orders_pages.route('/<order_id>', methods=['GET'])
@jwt_token_middleware
def get(order_id):
    pass


@orders_pages.route('/<order_id>', methods=['DELETE'])
def delete(order_id):
    pass


@orders_pages.route('/<order_id>', methods=['PUT'])
@jwt_token_middleware
def update(order_id):
    pass


@orders_pages.route('/', methods=['POST'])
@jwt_token_middleware
def post():
    pass


@orders_pages.route('/metrics', methods=['GET'])
@jwt_token_middleware
def metrics():
    pass
