from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
import os

# Create database instance
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Basic configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Secret key for sessions (required)
    app.config['SECRET_KEY'] = 'super-secret-key-change-later'

    # Configure server-side sessions
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    return app
