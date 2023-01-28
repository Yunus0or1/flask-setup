from flask import Flask
from util.dbconection import db
from util.config import Config


config = Config()
config.verify()

app = Flask(__name__)
app.config[config.DB_URI_TYPE] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.app_context().push()

db.init_app(app)


def addBluePrints():
    from orders import orders_pages
    app.register_blueprint(orders_pages)


def createTables():
    from models.orders import Orders
    from models.products import Products
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    createTables()
    addBluePrints()
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
