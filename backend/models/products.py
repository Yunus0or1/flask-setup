from util.dbconection import db


class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    list_price = db.Column(db.String(100), nullable=False)
    orders = db.relationship(
        "orders", backref="products", cascade="all, delete")

    def __repr__(self):
        return f'<Product => {self.id}>'
