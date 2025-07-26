import pytest
from app import app as flask_app, db


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    # Setup: configure the app for testing
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Use an in-memory SQLite DB
        "WTF_CSRF_ENABLED": False,  # Disable CSRF for tests
        "SECRET_KEY": "test-secret-key"
    })

    with flask_app.app_context():
        db.create_all()

    yield flask_app

    with flask_app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
