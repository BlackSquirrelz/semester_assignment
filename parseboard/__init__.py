# Database requirements
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Deployed Server Settings
import json
import urllib3

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from parseboard.main.routes import main
    app.register_blueprint(main)

    return app
