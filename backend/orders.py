from flask import Blueprint
from middlewares.user_required import user_required
from models.orders import Orders

orders_pages = Blueprint('orders', __name__, url_prefix='/orders')



@orders_pages.route('/', methods=['GET'])
@user_required
def list_orders():
    print(Orders.query.all())
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


