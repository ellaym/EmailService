# app/__init__.py
from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

mail = Mail()


def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask application, sets up Flask-Mail configuration,
    registers blueprints or routes, and returns the created app.

    Returns:
        app (Flask): The Flask application object.
    """
    load_dotenv()  # Load environment variables from .env file

    app = Flask(__name__)
    
    # Flask-Mail configuration
    app.config["MAIL_SERVER"] = os.getenv("SMTP_SERVER")
    app.config["MAIL_PORT"] = int(os.getenv("SMTP_PORT", 587))
    app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER")
    app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASS")
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False

    mail.init_app(app)

    # Register blueprints or routes
    from app.routes import main

    app.register_blueprint(main)

    return app
