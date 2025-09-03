from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import db
from app.models import Product
from app.forms import ProductForm

# Create a Blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    products = Product.query.all()
    return render_template('index.html', title='Página Inicial', products=products)

# Note que usamos @bp.route em vez de @app.route
@bp.route('/produto/adicionar', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('main.index')) # Use 'blueprint_name.function_name'
    return render_template('product_form.html', title='Adicionar Produto', form=form)

@bp.route('/produto/editar/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm()
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        db.session.commit()
        flash('As informações do produto foram atualizadas!', 'success')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
    return render_template('product_form.html', title='Editar Produto', form=form)

@bp.route('/produto/excluir/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product_to_delete = Product.query.get_or_404(product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('main.index'))