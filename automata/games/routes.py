from flask import jsonify
from automata.games import games_bp

@games_bp.route("/games")
def getAllGames():
   return jsonify([])

@games_bp.route('/games/<int:game_id>')
def getGame(game_id):
    return jsonify({ 'game': game_id })

