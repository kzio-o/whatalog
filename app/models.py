from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, index=True)
    phone = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True, index=True)
    customer_type = db.Column(db.Text)  # E.g.: CPF, Loja, Distribuidora

    __table_args__ = ({'sqlite_strict': True},)

    def __repr__(self):
        return f'<Customer {self.name}>'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.REAL, nullable=False)

    __table_args__ = ({'sqlite_strict': True},)


    # Relação com imagens (será implementado depois, mas já deixamos a base)
    # images = db.relationship('ProductImage', backref='product', lazy='dynamic')

    def __repr__(self):
        return f'<Product {self.name}>'
