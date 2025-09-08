from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import db
from app.models import Product, Customer
from app.forms import ProductForm, CustomerForm

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
        return redirect(url_for('main.index'))  # Use 'blueprint_name.function_name'
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


@bp.route('/clientes')
def customers():
    """Show a list of all customers."""
    customer_list = Customer.query.order_by(Customer.name).all()
    return render_template('customers.html', title='Clientes', customer_list=customer_list)


@bp.route('/cliente/adicionar', methods=['GET', 'POST'])
def add_customer():
    """Add a new customer."""
    form = CustomerForm()
    if form.validate_on_submit():
        new_customer = Customer(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            customer_type=form.customer_type.data
        )
        db.session.add(new_customer)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!')
        return redirect(url_for('main.customers'))
    return render_template('customer_form.html', title='Adicionar Cliente', form=form)


@bp.route('/cliente/editar/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    """Edit a customer."""
    customer = Customer.query.get_or_404(customer_id)
    form = CustomerForm()
    if form.validate_on_submit():
        customer.name = form.name.data
        customer.phone = form.phone.data
        customer.email = form.email.data
        customer.customer_type = form.customer_type.data
        db.session.commit()
        flash('Cliente atualizado com sucesso!')
        return redirect(url_for('main.customers'))
    elif request.method == 'GET':
        form.name.data = customer.name
        form.phone.data = customer.phone
        form.email.data = customer.email
        form.customer_type.data = customer.customer_type
    return render_template('customer_form.html', title='Editar Cliente', form=form)


@bp.route('/cliente/excluir/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    # """Delete a customer"""
    customer_to_delete = Customer.query.get_or_404(customer_id)
    db.session.delete(customer_to_delete)
    db.session.commit()
    flash('Cliente excluído com sucesso!')
    return redirect(url_for('main.customers'))
