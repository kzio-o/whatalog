from app.models import Customer
from app import db


def test_customer_list_page(client):
    """Test that the customer list page loads correctly."""
    response = client.get('/clientes')
    assert response.status_code == 200
    assert b"Lista de Clientes" in response.data


def test_add_customer(client, app):
    """Test GET requests"""
    response = client.get('/cliente/adicionar')
    assert response.status_code == 200

    response = client.post('/cliente/adicionar', data={
        'name': 'Test Customer',
        'phone': '1234567890',
        'email': 'test@example.com',
        'customer_type': 'Test Type'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Cliente cadastrado com sucesso!" in response.data

    with app.app_context():
        customer = Customer.query.filter_by(name='Test Customer').first()
        assert customer.email == 'test@example.com'
