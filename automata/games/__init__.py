from flask import Blueprint
from flask_restful import Api

# Create a blueprint
games_bp = Blueprint('games', __name__)
api = Api(games_bp)

# Import module routes
from automata.games import routes
from automata.games import game

