from flask import Blueprint, jsonify
from middlewares.jwt_token_middleware import jwt_token_middleware
from models.orders import Orders
from models.products import Products
from flask import request, jsonify, make_response
from util.helpers import model_list_to_dict_helper
from util.dbconection import db

orders_pages = Blueprint('orders', __name__, url_prefix='/orders')


@orders_pages.route('/', methods=['GET'])
@jwt_token_middleware
def list_orders():
    try:
        # Query String
        product_id = request.args.get('product_id')

        if product_id is None:
            orders = Orders.query.all()
        else:
            orders = Orders.query.filter(Orders.product_id == product_id)

        result = model_list_to_dict_helper(orders)
        return make_response(jsonify({"orders": result, "product_id": product_id}), 200)
    except Exception as e:
        print(e)
        return sendErrorResponse()


@orders_pages.route('/<order_id>', methods=['GET'])
@jwt_token_middleware
def get(order_id):
    try:
        order = Orders.query.get(order_id)
        if order:
            return make_response(jsonify({"order": order.as_dict()}), 200)
        return make_response(jsonify({"order": None}), 200)
    except Exception as e:
        print(e)
        return sendErrorResponse()


@orders_pages.route('/<order_id>', methods=['DELETE'])
def delete(order_id):
    try:
        Orders.query.filter(Orders.id == order_id).delete()
        db.session.commit()
        return make_response(jsonify({"message": "success"}), 200)
    except Exception as e:
        print(e)
        return sendErrorResponse()


@orders_pages.route('/<order_id>', methods=['PUT'])
@jwt_token_middleware
def update(order_id):
    try:
        request_data = request.get_json()
        actual_price = request_data['actual_price']

        order = Orders.query.get(order_id)

        if order is None:
            return sendCustomErrorResponse(title="Order is not found")

        order.actual_price = actual_price
        db.session.commit()

        return make_response(jsonify({"message": "success"}), 200)
    except Exception as e:
        print(e)
        return sendErrorResponse()


@orders_pages.route('/', methods=['POST'])
@jwt_token_middleware
def post():
    try:
        request_data = request.get_json()
        product_id = request_data['product_id']
        actual_price = request_data['actual_price']

        product = Products.query.get(product_id)
        if product is None:
            return sendCustomErrorResponse(title="Product is not found")

        order = Orders(actual_price=actual_price, product_id=product_id)
        db.session.add(order)
        db.session.commit()

        return make_response(jsonify({"message": "success"}), 200)
    except Exception as e:
        print(e)
        return sendErrorResponse()


@orders_pages.route('/metrics', methods=['GET'])
@jwt_token_middleware
def metrics():
    pass


def sendErrorResponse():
    return make_response(jsonify({"message": "Something went wrong."}), 500)


def sendCustomErrorResponse(title):
    return make_response(jsonify({"message": title}), 200)
