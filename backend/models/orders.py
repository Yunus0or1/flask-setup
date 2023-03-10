from util.dbconection import db

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    actual_price = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<Order => {self.id}>'
