from flask import Blueprint

# Create a blueprint
games_bp = Blueprint('games', __name__)

# Import module routes
from automata.games import routes

