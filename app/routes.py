from flask import render_template, flash, redirect, url_for, request
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

@app.route('/produto/editar/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    # Get the product from the DB by its ID, or return 404 error if not found
    product = Product.query.get_or_404(product_id)
    form = ProductForm()

    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        db.session.commit()
        flash('As informacoes do produto foram atualizadas com sucesso!', 'success')
        return redirect(url_for('index'))

    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price

    return render_template('product_form.html', title='Editar Produto', form=form)

@app.route('/produto/deletar/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product_to_delete = Product.query.get_or_404(product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    flash('Produto deletado com sucesso!', 'success')
    return redirect(url_for('index'))