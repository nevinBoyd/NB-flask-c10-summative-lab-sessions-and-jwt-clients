from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Session config
    app.config['SECRET_KEY'] = 'super-secret-key-change-later'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    # Initialize extensions
    Session(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app
