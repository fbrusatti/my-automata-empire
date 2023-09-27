from flask import Flask
from config import config

def create_app(config_name='development'):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_modules(app)

    return app

def register_modules(app):
    from automata.games import games_bp

    app.register_blueprint(games_bp)
