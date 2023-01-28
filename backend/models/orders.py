from util import dbconection

db = dbconection.db


class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    actual_price = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.String(100), db.ForeignKey('products.id'),)

    def __repr__(self):
        return f'<orders {self.id}>'
