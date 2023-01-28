from util.dbconection import db


class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2500), nullable=False)
    list_price = db.Column(db.Integer, nullable=False)
    orders = db.relationship(
        "Orders", backref="products", cascade="all, delete")

    def __repr__(self):
        return f'<Product => {self.id}>'
