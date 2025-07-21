from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True, index=True)
    customer_type = db.Column(db.String(50))  # E.g.: CPF, Loja, Distribuidora

    def __repr__(self):
        return f'<Customer {self.name}>'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

    # Relação com imagens (será implementado depois, mas já deixamos a base)
    # images = db.relationship('ProductImage', backref='product', lazy='dynamic')

    def __repr__(self):
        return f'<Product {self.name}>'
