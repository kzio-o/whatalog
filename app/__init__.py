import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #TODO: remover "or"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../instance/whatalog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Opcional

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
