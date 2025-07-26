from app.models import Product


def test_index_page_loads_correctly(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
    """

    response = client.get('/')
    response_text = response.data.decode('utf-8')

    assert response.status_code == 200
    assert "Catálogo de Produtos" in response_text # Decodes text for the especial characters
    assert b"Adicionar Novo Produto" in response.data

def test_index_page_shows_product(client, app):
    """
        GIVEN a product created in the database
        WHEN the '/' page is requested (GET)
        THEN check that the product is displayed
    """

    # Setup: Create a product in the in-memory database
    product = Product(name="Test Product", description="Test Description", price=10.99)
    with app.app_context():
        from app import db
        db.session.add(product)
        db.session.commit()

    # Action
    response = client.get('/')

    # Assert
    assert response.status_code == 200
    assert b"Test Product" in response.data
    assert b"Test Description" in response.data
    assert b"R$ 10.99" in response.data
