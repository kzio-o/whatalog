from flask import render_template
from app import app
from app.models import Product


@app.route("/")
@app.route("/index")
def index():
    products = Product.query.all()
    return render_template('index.html', title='Pagina inicial', products=products)
