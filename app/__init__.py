# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    # Register API routes from routes.py
    from .routes import register_routes
    register_routes(api)

    return app

# Create app instance
app = create_app()
