from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Product
from app.forms import ProductForm

@app.route("/")
@app.route("/index")
def index():
    products = Product.query.all()
    return render_template('index.html', title='Pagina inicial', products=products)

@app.route('/produto/adicionar', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        # Se o formulário for válido, cria o produto e salva no banco
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('index')) # Redireciona para a página inicial

    # Se for um GET, apenas mostra a página com o formulário
    return render_template('product_form.html', title='Adicionar Produto', form=form)