import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import event

# Initialize extensions without an app instance
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=None):
    """Creates and configures an instance of the Flask application."""
    app = Flask(__name__)

    # --- Load Configuration ---
    if config_class:
        app.config.from_object(config_class)
    else:
        # Default configuration for development
        basedir = os.path.abspath(os.path.dirname(__file__))
        load_dotenv(os.path.join(basedir, '../.env'))

        app.config.update(
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
                                    'sqlite:///' + os.path.join(basedir, '../instance/whatalog.db'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    # --- STEP 1: Initialize extensions WITH the app instance FIRST ---
    db.init_app(app)
    migrate.init_app(app, db)

    # --- STEP 2: NOW that db is initialized, you can safely access its engine ---
    # Configure PRAGMAs for SQLite
    with app.app_context():
        engine = db.engine

        @event.listens_for(engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            # Ativa o modo WAL para melhor concorrência
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            # Ativa a checagem de chaves estrangeiras para integridade dos dados
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

    # --- STEP 3: Register blueprints (and import models) ---
    from app import routes, models
    app.register_blueprint(routes.bp)

    return app