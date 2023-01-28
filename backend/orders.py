from flask import Blueprint
from models import orders

orders_pages = Blueprint('orders', __name__, url_prefix='/orders')



@orders_pages.route('/', methods=['GET'])
def list_orders():
    print(orders.query.all())
    return '<h3>Test</h3>'
    pass


@orders_pages.route('/<order_id>', methods=['GET'])
def get(order_id):
    pass


@orders_pages.route('/<order_id>', methods=['DELETE'])
def delete(order_id):
    pass


@orders_pages.route('/<order_id>', methods=['PUT'])
def update(order_id):
    pass


@orders_pages.route('/', methods=['POST'])
def post():
    pass


@orders_pages.route('/metrics', methods=['GET'])
def metrics():
    pass


