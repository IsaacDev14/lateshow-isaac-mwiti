# config.py

# Configuration settings for the Flask application

class Config:
    # Use SQLite as the default database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

    # Disable tracking modifications to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
