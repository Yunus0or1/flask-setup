from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from util import dbconection
from util import config
from util import dbconection


config = config.Config()
config.verify()

app = Flask(__name__)
app.config[config.DB_URI_TYPE] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = dbconection.db
db.init_app(app)


def addBluePrints():
    from orders import orders_pages
    app.register_blueprint(orders_pages)


def createDb():
    from models.orders import Orders
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    createDb()
    addBluePrints()
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
